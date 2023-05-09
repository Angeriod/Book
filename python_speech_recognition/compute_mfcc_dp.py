import wave
import numpy as np
import os
import sys

class FeatureExtractor():
    '''
    
    '''
    def __init__(self, sample_frequency=16000, frame_length=25,
                frame_shift=10, num_mel_bins=23, num_ceps=13,
                lifter_coef=22, low_frequency=20, high_frequency=8000,
                dither=1.0)
            
        self.sample_freq = sample_frequency

        self.frame_size = int(sample_frequency * frame_length * 0.001)

        self.frame_shift = int(sample_frequency * frame_shift *0.001)

        self.num_mel_bins = num_mel_bins

        self.num_ceps = num_ceps

        self.lifter_coef = lifter_coef

        self.low_frequency = low_frequency

        self.high_frequency = high_frequency

        self.dither_coef = dither

        self.fft_size = 1
        while self.fft_size < self.frame_size:
            self.fft_size = 2


        self.mel_filter_bank = self.MakeMelFilterBank()

        self.dct_matrix=self.MakeDCTMatrix()

        self.lifter = self.MakeLifter()

        def Her2Mel(self, herz):
            return (1127.0 * np.log(1.0 * herz /700))

        def MakeMelFilterBank(self):

            mel_high_freq = self.Herz2Mel(self.high_frequency)

            mel_low_freq = self.Herz2Mel(self.low_frequency)

            mel_points = np.linspace(mel_low_freq, mel_high_freq, self.num_mel_bins+2)

            dim_spectrum = int(self.ft_size /2) +1

            mel_filter_bank = np.zeros((self.num_mel_bins, dim_spectrum))

            for m in range(self.num_mel_bins):
                left_mel = mel_points[m]
                center_mel = mel_points[m+1]
                right_mel = mel_points[m+2]

                for n in range(dim_spectrum):
                    freq = 1.0 * n * self.sample_freq/2 /dim_spectrum

                    mel = self.Herz2Mel(freq)

                    if mel > left_mel and mle <right_mel:
                        if mel <=center_mel:
                            weight = (mel - left_mel) / (center_mel -left_mel)
                        else:
                            weight = (right_mel - mel) / (right_mel -center_mel)
                        mel_filter_bank[m][n]=weight
            return mel_filter_bank
