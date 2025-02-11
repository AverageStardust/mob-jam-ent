import json
from uuid import uuid4

def main():
    convert("ent_boss_model.bbmodel")

def convert(in_path):
    with open(in_path, "r") as in_file:
        model = json.load(in_file)
    
    for animation in model["animations"]:
        animators = animation["animators"]
        for animator_key in animators:
            animator = animators[animator_key]
            if animator["type"] == "bone":
                desc = animation["name"] + ", " + animator["name"]
                convert_animator(animator, desc)

    out_path = model["name"] + "_lin.bbmodel"
    with open(out_path, "w") as out_file:
        json.dump(model, out_file)

def convert_animator(animator, desc):
    keyframes_in = animator["keyframes"]
    time_start = keyframes_in[0]["time"]
    time_end = keyframes_in[-1]["time"]

    channels = {}
    for keyframe in keyframes_in:
        channel_key = keyframe["channel"]
        if channel_key in channels:
            channels[channel_key].append(keyframe)
        else:
            channels[channel_key] = [keyframe]
    
    keyframes_out = []
    for channel_key in channels:
        keyframes_out.append(convert_channel(channels[channel_key], desc))
    
    animator["keyframes"] = keyframes_out

def convert_channel(keyframes, desc):
    if len(keyframes) == 0:
        return []
    
    bez_sum = 0
    for keyframe in keyframes:
        if keyframe["interpolation"] == "bezier":
            bez_sum += 1
    
    if bez_sum <= 0:
        return keyframes

    if bez_sum < len(keyframes):
        raise Exception("Can't interpolate bezier and non-bezier keyframes in " + desc)


    for keyframe in keyframes:
        print(keyframe)

    # {'channel': 'position', 'data_points': [{'x': '0', 'y': '0.1', 'z': '0'}], 'uuid': 'c30164d5-f415-6135-0b20-7d898a8e15c1', 'time': 1.2083333333333333, 'color': -1, 'interpolation': 'bezier', 'bezier_linked': True, 'bezier_left_time': [-0.1, -0.01, -0.1], 'bezier_left_value': [0, -0.07619047619047618, 0], 'bezier_right_time': [0.1, 0.01, 0.1], 'bezier_right_value': [0, 0.07619047619047618, 0]}

    # {'channel': 'rotation', 'data_points': [{'x': '0', 'y': '0', 'z': '4'}], 'uuid': 'b6018b58-1675-a5c3-baa3-d0d25c3a178f', 'time': 0, 'color': -1, 'interpolation': 'linear'}

if __name__ == "__main__":
    main()