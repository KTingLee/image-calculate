import tool_images
import cv2
import os

def showPic (image, name = 'test'):
  cv2.imshow(name, image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def makeAnswerImages (path):
  pic = cv2.imread(path)
  erosion = tool_images.eraseImage(pic)
  blured = tool_images.blurImage(erosion)
  edged = tool_images.edgedImage(blured)
  charBox = tool_images.getCharBox(edged, 5, 40)
  # tool_images.showCharBox(blured, charBox)
  resizeImages = tool_images.resizeImage(blured, charBox)
  return resizeImages


if __name__ == '__main__':
  images = makeAnswerImages('../answer.png')
  folderPath = "../answers"

  try:
    os.makedirs(folderPath)
  except FileExistsError:
    print("資料夾已存在。")
  finally:
    for i, img in enumerate(images):
      imgName = str(i) if i < 10 else chr(i + 55)
      cv2.imwrite(folderPath + '/' + imgName + '.png', img)
      # pass