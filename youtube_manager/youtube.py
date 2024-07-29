
def list_all_videos(videos):
     pass

def add_video(videos):
    pass


def update_video(videos):
    pass

def delete_video(videos):
    pass

videos=[]

while True:
    print("\n youtube manager | choose a option")
    print("1.lit a favourite videos")
    print("2. add a youtube video")
    print("3. update ayoutube video details")
    print("4. delete a youtube video")
    print("5. exit the app")
    choice=input("enter your choice")

    match choice:
        case "1":
            list_all_videos(videos)
        case "2":
            add_video(videos)
        case "3":
            update_video(videos)
        case "4":
            delete_video(videos)
        case "5":
            break
        case _:
            print("invalid choice")
        