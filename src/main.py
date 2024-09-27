import os
from PIL import Image


def main():
	PATH_ORIGINALS = "originals"
	PATH_DERIVATIVES = "derivatives"

	for file in os.listdir(PATH_ORIGINALS):
		
		try:
			image = Image.open(f"{PATH_ORIGINALS}/{file}")
		except Exception as e:
			print(f"Skipping file ({e})")
			continue

		print(f"====>{file}({image.width}x{image.height})")
		widths_input = list(map(lambda width: width.strip(), input("List new widths by comma: ").split(",")))
		for width in widths_input:
			try:

				file_path = os.path.splitext(file)
				new_image_name = f"{file_path[0]}_{width}{file_path[1]}"
				new_image_width = int(width)
				new_image_height = int((new_image_width/image.width) * image.height)

				new_image = image.resize((new_image_width, new_image_height))
				new_image.save(f"{PATH_DERIVATIVES}/{new_image_name}")
				print(f"Created {PATH_DERIVATIVES}/{new_image_name}")

			except Exception as e:
				print(f"Skipping width ({e})")
				continue

if __name__ == "__main__":
	main()