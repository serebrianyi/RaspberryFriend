import subprocess


class DlnaHandler(object):

    def process(self):
        proc = subprocess.Popen("sudo service minidlna stop", shell=True)
        proc.wait()
        proc = subprocess.Popen("sudo minidlna -R", shell=True)
        proc.wait()
        proc = subprocess.Popen("sudo service minidlna start", shell=True)
        proc.wait()
        return "Dlna restarted"