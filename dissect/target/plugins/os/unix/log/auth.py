import re
from itertools import chain
from typing import Generator

from flow.record.fieldtypes import path

from dissect.target.helpers.fsutil import TargetPath
from dissect.target.helpers.record import TargetRecordDescriptor
from dissect.target.helpers.utils import year_rollover_helper
from dissect.target.plugin import Plugin, export

AuthLogRecord = TargetRecordDescriptor(
    "linux/log/auth",
    [
        ("datetime", "ts"),
        ("string", "message"),
        ("string", "source"),
    ],
)

_TS_REGEX = r"^[A-Za-z]{3}\s*[0-9]{1,2}\s[0-9]{1,2}:[0-9]{2}:[0-9]{2}"
RE_TS = re.compile(_TS_REGEX)
RE_TS_AND_HOSTNAME = re.compile(_TS_REGEX + r"\s\w+\s")


class AuthPlugin(Plugin):
    def check_compatible(self):
        var_log = self.target.fs.path("/var/log")
        return any(var_log.glob("auth.log*")) or any(var_log.glob("secure*"))

    @export(record=[AuthLogRecord])
    def securelog(self):
        """Return contents of /var/log/auth.log* and /var/log/secure*."""
        return self.authlog()

    @export(record=[AuthLogRecord])
    def authlog(self):
        """Return contents of /var/log/auth.log* and /var/log/secure*."""

        # Assuming no custom date_format template is set in syslog-ng or systemd (M d H:M:S)
        # CentOS format: Jan 12 13:37:00 hostname daemon: message
        # Debian format: Jan 12 13:37:00 hostname daemon[pid]: pam_unix(daemon:session): message

        tzinfo = self.target.datetime.tzinfo

        var_log = self.target.fs.path("/var/log")
        for auth_file in chain(var_log.glob("auth.log*"), var_log.glob("secure*")):
            for ts, line in year_rollover_helper(auth_file, RE_TS, "%b %d %H:%M:%S", tzinfo):
                message = line.replace(re.search(RE_TS_AND_HOSTNAME, line).group(0), "").strip()
                yield AuthLogRecord(
                    ts=ts,
                    message=message,
                    source=path.from_posix(auth_file),
                    _target=self.target,
                )
