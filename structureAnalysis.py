import Image
from models import Path

def binarizeImage(img, threshold=128):
  if img.mode != 'L':
    img = img.convert('L')
  new_img = Image.new(img.mode, img.size)
  for i in range(new_img.size[0]):
    for j in range(new_img.size[1]):
      if img.getpixel((i,j)) <= threshold:
        new_img.putpixel((i,j), 0)
      else:
        new_img.putpixel((i,j), 255)
  return new_img

def westAndEastAnalysis(img, pixel, pixel_list, target_color):
  if (pixel[1]-1 > 0):
    if img.getpixel((pixel[0],pixel[1]-1)) == target_color:
      pixel_list.append((pixel[0], pixel[1]-1))

  if (pixel[1]+1 < img.size[1]):
    if img.getpixel((pixel[0],pixel[1]+1)) == target_color:
      pixel_list.append((pixel[0], pixel[1]+1))

# remover o retorno da imagem
def floodFill(img, seed, target_color, replace_color):
  q_pixel_list = []
  path = Path(replace_color)

  if img.getpixel(seed) == target_color:
    q_pixel_list.append(seed)
    while q_pixel_list:
      pixel_list = []
      for ele in q_pixel_list:
        if img.getpixel(ele) == target_color:
          path.setMinHoriz(ele[0])
          path.setMaxHoriz(ele[0])
          path.setMinVert(ele[1])
          path.setMaxVert(ele[1])
          img.putpixel(ele, replace_color)
          path.incArea()

          westAndEastAnalysis(img, ele, pixel_list, target_color)
          w = e = ele
          while (w[0] > 0):
            if img.getpixel((w[0]-1, w[1])) == target_color:
              path.setMinHoriz(w[0]-1)
              img.putpixel((w[0]-1, w[1]), replace_color)
              path.incArea()

              if (w[1]-1 >= 0):
                if img.getpixel((w[0]-1,w[1]-1)) == target_color:
                  path.setMinVert(w[1]-1)
                  pixel_list.append((w[0]-1, w[1]-1))

              if (w[1]+1 < img.size[1]-1):
                if img.getpixel((w[0]-1,w[1]+1)) == target_color:
                  path.setMaxVert(w[1]+1)
                  pixel_list.append((w[0]-1, w[1]+1))

              w = (w[0]-1, w[1])
            else:
               break

          while (e[0] < img.size[0]-1):
            if img.getpixel((e[0]+1, e[1])) == target_color:
              img.putpixel((e[0]+1, e[1]), replace_color)
              path.incArea()
              path.setMaxHoriz(e[0]+1)

              if (e[1]-1 >= 0):
                if img.getpixel((e[0]+1,e[1]-1)) == target_color:
                  pixel_list.append((e[0]+1, e[1]-1))
                  path.setMinVert(e[1]-1)

              if (e[1]+1 < img.size[1]-1):
                if img.getpixel((e[0]+1,e[1]+1)) == target_color:
                  pixel_list.append((e[0]+1, e[1]+1))
                  path.setMaxVert(e[1]+1)

              e = (e[0]+1, e[1])
            else:
               break
      q_pixel_list = pixel_list
  return (img, path)

def analysis(img, target_color=255):
  path_number = -1
  color = 10
  path_list = []
  for i in range(img.size[0]):
    for j in range(img.size[1]):
      if img.getpixel((i,j)) == target_color:
        path_number = path_number + 1
        result = floodFill(img, (i,j), target_color, color)

        path_list.append(result[1])
        color=color+5

  return (result, path_list)

def intercepto(img, porous_color=255, solid_color=0, eliminate_board=True):
  lines_segmented = []
  rows_segmented = []
  porous_list_horizontal = []
  solid_list_horizontal = []
  porous_list_vertical = []
  solid_list_vertical = []

  for line in range(img.size[1]):
    segmented_list = []
    color_sequence = img.getpixel((0,line))
    new_list = []
    for row in range(img.size[0]):
      if img.getpixel((row, line)) == color_sequence:
        new_list.append((row, line))
      else:
        segmented_list.append(new_list)
        new_list = []
        color_sequence = img.getpixel((row, line))
        new_list.append((row, line))
    segmented_list.append(new_list)

    if eliminate_board:
      lines_segmented.append(segmented_list[1:-1])
    else:
      lines_segmented.append(segmented_list)

  for row in range(img.size[0]):
    segmented_list = []
    color_sequence = img.getpixel((row, 0))
    new_list = []

    for line in range(img.size[1]):
      if img.getpixel((row, line)) == color_sequence:
        new_list.append((row, line))
      else:
        segmented_list.append(new_list)
        new_list = []
        color_sequence = img.getpixel((row, line))
        new_list.append((row, line))
    segmented_list.append(new_list)

    if eliminate_board:
      rows_segmented.append(segmented_list[1:-1])
    else:
      rows_segmented.append(segmented_list)

  for line in lines_segmented:
    for group in line:
      if img.getpixel(group[0]) == solid_color:
        solid_list_horizontal.append(len(group))
      else:
        porous_list_horizontal.append(len(group))

  for row in rows_segmented:
    for group in row:
      if img.getpixel(group[0]) == solid_color:
        solid_list_vertical.append(len(group))
      else:
        porous_list_vertical.append(len(group))

  return {"porous_list_vertical":porous_list_vertical,
  "porous_list_horizontal":porous_list_horizontal,
  "solid_list_horizontal":solid_list_horizontal,
  "solid_list_vertical":solid_list_vertical,
  "row_group_list":rows_segmented,
  "line_group_list":lines_segmented}

