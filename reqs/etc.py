
import subprocess

class MemoryMonitor(object):

    def __init__(self, username):
        """Create new MemoryMonitor instance."""
        self.username = username

    def usage(self):
        """Return int containing memory used by user's processes."""
        self.process = subprocess.Popen("ps -u %s -o rss | awk '{sum+=$1} END {print sum}'" % self.username,
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        )
        self.stdout_list = self.process.communicate()[0].split('\n')
        return int(self.stdout_list[0])


memory_mon = MemoryMonitor('root')
used_memory = memory_mon.usage()