"""
run_HR_detection.py


Main running script for analyzing heart rate data.
Uses external functions for all processes to allow easy replacement
"""


def main():

    import signal_processing as sp

    [t, v] = sp.load_CSV("ziva.csv")
    filt_v = sp.HP_filter(t, v, 10, 9)
    mask = sp.threshold_find_peaks(t, filt_v, .97)
    bpm = sp.calc_bpm(t, mask)
    [t_beat, avg_beat] = sp.calc_average_beat(t, v, mask, bpm)
    
    mask_corrected = sp.verify_peaks_ncc(v, mask, avg_beat)
    sp.display_trace(t, v, [20, 30], [], True, mask_corrected)
    [t_beat_corrected, avg_beat_corrected] = sp.calc_average_beat(t, v, mask_corrected, bpm)
    sp.display_trace(t_beat_corrected, avg_beat_corrected)
    bpm_corrected = sp.calc_bpm(t, mask_corrected)
    print(bpm_corrected,"beats per minute")
    
if __name__ == '__main__':
    main()
