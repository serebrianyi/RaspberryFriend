import subprocess


class DlnaHandler(object):

    def process(self):
        # stop the service
        proc = subprocess.Popen("sudo service minidlna stop", shell=True)
        proc.wait()
        # rescan the folder content
        proc = subprocess.Popen("sudo minidlna -R", shell=True)
        proc.wait()
        # start the service
        proc = subprocess.Popen("sudo service minidlna start", shell=True)
        proc.wait()
        return {"message_text": "Dlna restarted"}