#use of flush command in file
#used to force to write into the file

file = open(r"D:\Python\Codding\File_ Handling\ my_file_5.txt","w")

file.write("This is my ne flush to the file\n")     # this will keep this into the buffer into the buffer not in the file directly 
                                                    # It will be decided by the os wether to write in to the physical file or not
                                                    #if the programme got crashed the write command
                                                    # doesn't garrantee that buffer is flushed into the file or not
file.flush()        #Write immediately into the file  
file.close()