import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def create_or_update_broadcast():
    client_id = os.environ.get("YOUTUBE_CLIENT_ID")
    client_secret = os.environ.get("YOUTUBE_CLIENT_SECRET")
    refresh_token = os.environ.get("YOUTUBE_REFRESH_TOKEN")
    next_id = os.environ.get("NEXT_ID")
    
    # JSON ဖိုင်မှ ဒေတာများဖတ်ရန် (သို့မဟုတ် အောက်ပါ Default တန်ဖိုးများကို တိုက်ရိုက်သုံးရန်)
    video_item = None
    if os.path.exists("work/main.json"):
        with open("work/main.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                if str(item.get("id")) == str(next_id):
                    video_item = item
                    break
                    
    # အကယ်၍ JSON ထဲတွင် မတွေ့ပါက သို့မဟုတ် Default အသုံးချလိုပါက အောက်ပါအတိုင်း သတ်မှတ်မည်
    if video_item:
        title = video_item.get("title")
        description = video_item.get("description")
        tags = video_item.get("video_tags", [])
    else:
        # သင်ပေးထားသော Default တန်ဖိုးများ
        title = "တစ်နေ့တာအတွက် ကံကောင်းခြင်းများစွာ ပိုင်ဆိုင်ဖို့ - မဟာသမယသုတ် တရားတော် 🔴🙏"
        description = (
            "နံနက်ခင်းအချိန်တွင် ပဋ္ဌာန်းပါဠိတော်နှင့် မဟာသမယသုတ် တရားတော်များကို နာယူခြင်းဖြင့် စိတ်ချမ်းသာမှုနှင့် "
            "ကံပွင့်လာဘ်ပွင့် စီးပွားတက်စေရန် ရည်ရွယ်ပါသည်။\n\n"
            "ဤဗီဒီယိုတွင် မြတ်စွာဘုရားရှင်၏ ရုပ်ပွားတော်အား ရွှေရောင်အလင်းတန်းများဖြင့် တင့်တယ်စွာ ပူဇော်ထားပြီး "
            "ပဋ္ဌာန်းပါဠိတော်များကို ရွတ်ဖတ်သရဇ္ဈာယ်ထားသည့် တရားတော်များကို နာယူနိုင်ပါသည်။ ပဋ္ဌာန်းပါဠိတော်ကို နာယူမှတ်သားခြင်းသည် "
            "မိမိတို့၏ စိတ်နှလုံးကို အေးချမ်းစေပြီး ကုသိုလ်တရားများ တိုးပွားစေသည့် အလွန်မွန်မြတ်သော အလေ့အကျင့်တစ်ခု ဖြစ်ပါသည်။ "
            "နေ့စဉ် နံနက်ခင်းတိုင်းတွင် ဤတရားတော်များကို နာယူခြင်းဖြင့် မိမိတို့၏ ဘဝအတွက် ကောင်းမွန်သော စိတ်ဓာတ်ခွန်အားများကို "
            "ရရှိစေမည် ဖြစ်ပါသည်။\n\n"
            "ထို့အပြင် မဟာသမယသုတ် တရားတော်များကို နာယူခြင်းသည် ဘေးအန္တရာယ်ကင်းရှင်းပြီး စိတ်၏ချမ်းသာခြင်း၊ "
            "ကိုယ်၏ကျန်းမာခြင်းကို ဖြစ်ပေါ်စေပါသည်။ ဤတရားတော်များသည် ကံပွင့်လာဘ်ပွင့်စေရန်နှင့် စီးပွားရေးလုပ်ငန်းများ "
            "အဆင်ပြေချောမွေ့စေရန် ရည်ရွယ်၍ ပူဇော်ထားခြင်း ဖြစ်ပါသည်။ တရားချစ်ခင်သူတော်စင်များအနေဖြင့် ဤတရားတော်များကို "
            "အချိန်ပေး၍ နာယူခြင်းဖြင့် မိမိတို့၏ ဘဝလမ်းကြောင်းတွင် ကောင်းကျိုးများ ရရှိလာစေရန် ရည်ရွယ်ပါသည်။\n\n"
            "ဓမ္မမိတ်ဆွေများအနေဖြင့် တရားတော်များကို ဆက်လက်နာယူနိုင်ရန်အတွက် ချန်နယ်ကို Subscribe လုပ်ထားပေးပါရန် "
            "ဖိတ်ခေါ်အပ်ပါသည်။ နောင်တွင်လည်း တင်ဆက်ပေးမည့် တရားတော်များကို အတူတူ နာယူပူဇော်ကြပါစို့။"
        )
        tags = [
            "ကံပွင့်လာဘ်ပွင့်",
            "မဟာသမယသုတ်တရားတော်",
            "ပဋ္ဌာန်းပါဠိတော်",
            "ပရိတ်ကြီး၁၁သုတ်",
            "စီးပွားတက်တရားတော်",
            "နံနက်ခင်းတရားတော်",
            "မေတ္တာပို့တရားတော်",
            "ပါချုပ်ဆရာတော်ဘုရားကြီးတရားတော်များ",
            "မင်းကွန်းဆရာတော်တရား",
            "ဓမ္မစကြာတရားတော်",
            "ဂုဏ်တော်ကိုးပါး",
            "လာဘ်ပွင့်ဂါထာတော်",
            "အစွမ်းထက်ဂါထာတော်",
            "ဘေးအန္တရာယ်ကင်းပရိတ်တရားတော်",
            "ပဌာန်းဒေသနာတော်",
            "တရားတော်များ 2026",
            "တရားတော်များ",
            "dhamma channel myanmar",
            "buddha chanting myanmar",
            "daily dhamma teaching",
            "myanmar buddhist prayer",
            "morning prayer blessings",
            "pali chanting for peace",
            "dhammatalk",
            "tayar taw myanmar"
        ]

    creds = Credentials(
        None,
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        token_uri="https://oauth2.googleapis.com/token"
    )
    
    youtube = build("youtube", "v3", credentials=creds)
    
    # 1. YouTube Live Broadcast အသစ်ဖန်တီးခြင်း (Insert)
    print("Creating new YouTube Live Broadcast...")
    broadcast_request = youtube.liveBroadcasts().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "scheduledStartTime": "2026-09-22T00:00:00Z"  # လိုအပ်ပါက အချိန်အမှန်သို့ ပြောင်းလဲနိုင်ပါသည်
            },
            "status": {
                "privacyStatus": "public",  # public, unlisted သို့မဟုတ် private
                "selfDeclaredMadeForKids": False
            }
        }
    )
    broadcast_response = broadcast_request.execute()
    broadcast_id = broadcast_response["id"]
    print(f"Successfully created Broadcast ID: {broadcast_id}")
    
    # 2. Tags နှင့် Category များကို Update လုပ်ခြင်း (liveBroadcasts.update ကိုသုံးခြင်း)
    try:
        youtube.liveBroadcasts().update(
            part="snippet",
            body={
                "id": broadcast_id,
                "snippet": {
                    "title": title,
                    "description": description,
                    "categoryId": "24",  # Entertainment category
                    "scheduledStartTime": broadcast_response["snippet"]["scheduledStartTime"]
                }
            }
        ).execute()
        print("Broadcast snippet updated successfully.")
    except Exception as e:
        print(f"Warning: Broadcast update failed: {e}")

    # 3. Thumbnail တင်ခြင်း
    if next_id:
        padded_id = f"{int(next_id):05d}"
        thumb_path = f"work/{padded_id}.jpg"
        
        if os.path.exists(thumb_path):
            print(f"Uploading thumbnail for broadcast {broadcast_id}...")
            youtube.thumbnails().set(
                videoId=broadcast_id,
                media_body=MediaFileUpload(thumb_path)
            ).execute()
            print("Thumbnail uploaded successfully.")

if __name__ == "__main__":
    create_or_update_broadcast()
