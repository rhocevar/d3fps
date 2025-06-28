import sys
import os
import json

def read_data_for_act(dir_path):
    data_list = []
    for filename in os.listdir(dir_path):
        # This condition can be optimized to only consider files of a specific act based on the file name
        if filename.endswith(".json"):
            file_path = os.path.join(dir_path, filename)
            try:
                with open(file_path, 'r') as json_file:
                    json_data = json.load(json_file)
                    data_list.append(json_data)
            except Exception as e:
                print(f"There was a problem reading file {file_path}: {e}")
    return data_list

def get_fps_samples_for_act(logs, act):
    fps_samples = []
    for log in logs:
        for collection in log["collections"]:
            if collection['act'] == act:
                samples = collection['samples']
                for sample in samples:
                    fps_samples.append(sample['fps'])
    return fps_samples

def calculate_min_max_fps(fps_samples):
    min_fps = min(fps_samples)
    max_fps = max(fps_samples)

    return min_fps, max_fps

def calculate_avg_fps(fps_samples):
    n_samples = len(fps_samples)
    if n_samples == 0:
        return 0

    avg_fps = 0
    for fps in fps_samples:
        avg_fps += fps

    avg_fps /= n_samples

    return avg_fps

def analyze_fps_from_logs(act, calc_type, data_dir):
    # 1. Read arguments from the command line
    print(f"Arguments: act = {act}, calc_type = {calc_type}, data_dir = {data_dir}")

    # 2. Read JSON files contained in data_dir
    fps_logs = read_data_for_act(data_dir)
    print(f"{len(fps_logs)} log files found in '{data_dir}'")

    # 3. Read list of FPS samples for act
    fps_samples = get_fps_samples_for_act(fps_logs, act)
    print(f"{len(fps_samples)} fps samples found for act '{act}'")

    # 4. Perform calculation based on 'calc_type' and print result
    match calc_type:
        case "minmax":
            result = calculate_min_max_fps(fps_samples)
            print(f"Min FPS: {result[0]}, Max FPS: {result[1]}")
        case "avg":
            result = calculate_avg_fps(fps_samples)
            print(f"Average FPS: {result}")
        case _:
            raise Exception(f"Unknown calc_type '{calc_type}'")

if __name__ == '__main__':
    print("D3 FPS (Frames Per Second) Analysis")
    analyze_fps_from_logs(sys.argv[1], sys.argv[2], sys.argv[3])

# Possible inputs --> results
# > d3fps A1 minmax ./FPSLogs --> Min FPS: 37.84, Max FPS: 61.96
# > d3fps A2 minmax ./FPSLogs --> Min FPS: 19.44, Max FPS: 62.43
# > d3fps A3 minmax ./FPSLogs --> Min FPS: 2.87, Max FPS: 64.44
# > d3fps A4 minmax ./FPSLogs --> Min FPS: 3.81, Max FPS: 62.51

# > d3fps A1 avg ./FPSLogs --> Average FPS: 58.601446886446965
# > d3fps A2 avg ./FPSLogs --> Average FPS: 58.235093411996054
# > d3fps A3 avg ./FPSLogs --> Average FPS: 56.883329113924
# > d3fps A4 avg ./FPSLogs --> Average FPS: 53.82466251298041
