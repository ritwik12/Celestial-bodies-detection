#! python3
# rename_training_files.py - Will be used to rename all training data image files
# that are being used for a TensorFlow Celestial Body image classifier

import os, shutil

# Walk the directory tree to locate folder, subfolder, and filenames
for folderName, subfolders, filenames in os.walk('.\\training_data'):
	print('The current folder is ' + folderName)
	i = 0
	for filename in filenames:
		absWorkingDir = os.path.abspath('C:\\dev_projects\\contributions\\Celestial-bodies-detection\\hub\\examples\\image_retraining')
		print(absWorkingDir)
		src = os.path.join(absWorkingDir, folderName, filename)
		dst = os.path.join(absWorkingDir, folderName, str("{0:0=3d}".format(i))) + '.jpg'
		print('Renaming "%s" to "%s"...' % (src, dst))
		shutil.move(src, dst)
		i += 1