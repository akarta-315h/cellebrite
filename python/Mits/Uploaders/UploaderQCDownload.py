# uploader for Qualcomm DownloadMode 
from IUploader import IUploader
class UploaderQCDownload(IUploader):
        
        self.protocol.start_firmware_update()
        self.protocol.start_qcsbl()
        self.protocol.send_oemsbl_hd(oemsbl)
        self.protocol.shut()

    def upload_file(self, file_data):
    def upload_chunk(self, offset, data):