import os
import json
import sys
import uuid

modifications = [
    "There is a modification involving the addition of a beard. ",
    "There is a modification involving the addition of a pair of eyeglasses. ",
    "There is a modification making the person to appear to be smiling. ",
    "There is a modification making the person to appear younger than they really are. ",
    "There is a modification involving the addition of Bangs. "
    "There is no modification. "
]

# Function to get list of image files in the directory
def get_image_files(directory):
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_files.append(filename)
    return image_files

def get_idx(string):
    #print(string)
    deepfakes = [
        "Beard",
        "Eyeglasses",
        "Smiling",
        "Young",
        "Bangs",
        "original"
    ]
    for i in range(len(deepfakes)):
        if (deepfakes[i]==string):
            return i

#returns correct string
def get_answer(directory):
    tag = directory[68:len(directory)-1]
    #print(tag)
    ans=[]
    count = 0
    while (len(tag)>0):
        count+=1
        if (count>5): break
        x=tag.find('-')
        #print(x)
        if (x==-1):
            ans.append(get_idx(tag))
            break
        str=tag[0:x]
        tag=tag[x+1:]
        ans.append(get_idx(str))
        #print(ans)
    return ans
    

# Function to create JSON file with entries for each image file
def create_json(image_dir, json_file_path):
    # Get list of image files
    image_files = get_image_files(image_dir)

    # Create list of entries for each image file
    image_entries = []
    
    answer=""
    for i in get_answer(image_dir):
        answer=answer+modifications[i]
    
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        entry_id = str(uuid.uuid4())
        entry = {
            "id": entry_id,
            "image": image_path,
            "conversations": [
                {
                    "from": "human",
                    "value": "This image could possibly have deepfake modifications made to it." + " ".join(modifications) + "Thus your job is to figure out all the modifications. There is a specific order to them as well. Extraneous guesses will be penalized. Thus there is also a chance no modifications were made."
                },
                {
                    "from": "gpt",
                    "value": answer
                }
            ]
        }
        image_entries.append(entry)

    # Writing data to the JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(image_entries, json_file, indent=4)

    print("JSON file created successfully at", json_file_path)

# Check if the script is called with the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <image_directory> <json_output_file>")
    sys.exit(1)

# Get command-line arguments
image_dir = sys.argv[1] #directory path
json_file_path = sys.argv[2] #output path

# Check if the specified directory exists
if not os.path.isdir(image_dir):
    print("Error: The specified directory does not exist.")
    sys.exit(1)

# Call the function to create the JSON file
#print(image_dir)
#get_answer(image_dir)
create_json(image_dir, json_file_path)