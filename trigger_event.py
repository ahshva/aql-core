# trigger_event.py – AQL Event Trigger System

def trigger_event(event_name, details=""):
    print(f"🚨 حدث داخلي تم إطلاقه: {event_name}")
    if details:
        print("🔍 تفاصيل:", details)

# مثال:
# trigger_event("start_expansion", "خلية جديدة تم تنشيطها")
