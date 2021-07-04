from PIL import Image
import os

class image2pdf:
    def __init__(self):
        self.validFormats = (
            '.jpg',
            '.jpeg',
            '.png',
            '.JPG',
            '.PNG'
        )
        self.pictures = []
        self.files = os.listdir()
        self.convertPictures()
        input('Tamamlandı...(Çıkış için bir tuşa basın)')

    
    def filter(self, item):
        return item.endswith(self.validFormats)


    def sortFiles(self):
        return sorted(self.files)

    
    def getPictures(self):
        pictures = list(filter(self.filter, self.sortFiles()))
        if self.isEmpty(pictures):
        	print(" [Hata] Klasörde bir görsel bulunamadı ! ")
        	raise Exception(" [Hata] Klasörde bir görsel bulunamadı !")
        print('Resimler : \n {}'.format(pictures))
        return pictures

    def isEmpty(self, items):
    	return True if len(items) == 0 else False

    def convertPictures(self):
        for picture in self.getPictures():
            self.pictures.append(Image.open(picture).convert('RGB'))
        self.save()


    def save(self):
        self.pictures[0].save('Sonuc.pdf', save_all=True, append_images=self.pictures[1:])
    

if __name__ == "__main__":
    image2pdf()

###   Bu Proje Ali Rıza Fırat tarafından eğitim amaçlı olarak paylaşılmıştır.
###   https://alirizafirat.com/
###   alirizafirat@aol.com
