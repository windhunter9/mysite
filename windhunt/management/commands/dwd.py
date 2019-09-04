from cdo import Cdo
cdo = Cdo()
import ftplib
from ftplib import FTP
import io
from os.path import join
import bz2


def DownloadDWD():
	server = ftplib.FTP()

	# DWD FTP server host name
	server = "opendata.dwd.de"

	# FTP server path for our files
	serverpath = "/weather/nwp/icon-eu/grib/12/"
	# You don't have to print this, because this command itself prints dir contents 

	user = "anonymous"
	passwd = "guest@example.com"

	ftp = FTP(server)
	ftp.login(user, passwd)


	zonal_wind = "u_10m/"
	ftp.cwd(serverpath+zonal_wind)
	files_zonal = ftp.nlst()
	#print(files_zonal)

	meridional_wind ="v_10m/"
	ftp.cwd(serverpath+meridional_wind)
	files_meridional = ftp.nlst()
	#print(files_meridional)


	max_wind ="vmax_10m/"
	ftp.cwd(serverpath+max_wind)
	files_max_wind = ftp.nlst()

	#server.d11ir()#
	path_data = "/media/data/owncloud/code/julian_magnus/J_and_M/grib2/data/"
	path_grid = "/media/data/owncloud/code/julian_magnus/J_and_M/grib2/data/"

	file_grid = join(path_grid,'target_grid_world_025.txt' )
	file_weight = join(path_grid, 'weight.nc')
	ftp.cwd(serverpath)

	for i,file_max_wind in enumerate((files_max_wind)):
		if i > 50000:
			break
		else:
		    # Create byte stream
		    f = io.BytesIO()
		    # Retrieve .bz2 file from ftp server
		    ftp.retrbinary("RETR " +max_wind+ file_max_wind, f.write)
		    # Decompress .bz2 file
		    decompressed_file = bz2.decompress(f.getvalue())
		    #  write to folder
		    filename = join(path_data,file_max_wind[:-4])
		    file1 = open(filename, 'wb')
		    file1.write(decompressed_file);
		    outfile1 = join(path_data,"vmax"+str(i) + '.nc')
		    cdo.copy(\
		    	input = filename,\
		    	output = outfile1, options = '-f nc')
