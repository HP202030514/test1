from kivymd.app import MDApp

class MainApp(MDApp):
    source_file_name = 'temp.jpg'


    def take_image(self):
        from plyer import camera
        filepath = self.user_data_dir + '/' + 'temp.png'
        try:
            camera.take_picture(filename=filepath, on_complete=self.camera_callback)
        except NotImplementedError:
            print("Can't take a picture on this platform")

    def camera_callback(self, filepath):
        from os.path import exists
        if exists(filepath):
            print("Picture saved!", filepath)

        else:
            print("Couldnt save picture")


    def detect_handwriting(self):
        print("Detecting handwriting...")
        self.select_image()

    def select_image(self):
        # Select a file from your device
        self.take_image()
        # Upload the file

MainApp().run()