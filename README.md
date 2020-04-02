# Tweet Video Maker

This module takes in the names of various Twitter users, as well as a number of cycles the user would like to make a video for. It can be called multiple times for different users for a different number of cycles.

As a RESTful Flask site, when you input your search in the form of 'ip.address/<twitter_handle>/<number_of_cloud_images_wanted>', you will be prompted to download and view the video once it is completed. If it is unable to complete, you will be directed to an error page.

## How to use the maker

Be sure to install the 'arial.ttf' font and have it in the directory with all of these scripts. Without it, the Wordcloud will not be able to run, as it uses the font to write dates on each image.

For easy use download the EasyAccess folder, which is pre-arranged to have all components to the module, necessary fonts, and requirements. Also, download the four tests, along with the .json file for offline use.

If you already have your Twitter API keys stored in a file called 'keys' that is in the same directory as the main code, you can run the main process through tweet_queue.py. This script allows you to put in a list of N number of user handles and M number of cycles for each handle to have analyzed (see practice example in script). The module will then act on its own to process each cycle as a thread in the set queue until all threads are processed and a video for each handle is made.

To utilize the code, please check that you have downloaded all of the files in the EasyAccess folder. The file you will need to run is 'rest_twitter_redux.py'. NOTE: If you are running this locally, you will need to change the path name in line 18 (folderName) to the path you will be running the script from. If not, the script will not be able to find your video.

## Notes for how to run the script

When running locally, I personally found it effective to run it as such:

<code>export FLASK_APP=rest_twitter_redux.py </code><br>
<code>flask run</code>

Then I proceeded to use the local host link to begin my search test.

## How to access the RESTful API link

While the instance is active, you can access the API here: http://3.88.72.42
