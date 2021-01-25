from lib import tool_images
import cv2
import os

pics = os.listdir('./answers')
benchmarks = {}
for pic in pics:
  benchmarks[pic[0]] = cv2.imread('./answers/' + pic, cv2.IMREAD_GRAYSCALE)

def recogChar (char):
  minErr = 999999999
  result = None
  for key in benchmarks.keys():
    err = tool_images.diffPictures(char, benchmarks[key])
    if err < minErr:
      minErr = err
      result = key
  return result

def captchaSolver (path):
  pic = cv2.imread(path)
  erosion = tool_images.eraseImage(pic)
  blured = tool_images.blurImage(erosion)
  edged = tool_images.edgedImage(blured)
  dilated = tool_images.dilateImage(edged)
  charBox = tool_images.getCharBox(dilated)
  dilated = tool_images.dilateImage(edged, (4, 4))
  chars = tool_images.resizeImage(dilated, charBox)

  result = []
  for char in chars:
    result.append(recogChar(char))
  imgName = ''.join(result)
  return imgName

if __name__ == '__main__':
  pics = os.listdir('./img')
  def filterJPG (name):
    if '.jpg' in name:
      return name
  pics = filter(filterJPG, pics)
  i = 0
  for pic in pics:
    if i < 300:
      path = './img/'
      imgName = captchaSolver(path + pic)
      os.rename(os.path.join(path, pic), os.path.join(path, imgName + '.jpg'))
    i += 1
