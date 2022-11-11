from ctypes import sizeof
import streamlit as st
import librosa
from librosa import display
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import time
import datetime
import plotly.graph_objects as go
import plotly.express as px


plt.rcParams.update({
  'font.size' : 10
  ,'font.family' : 'Meiryo' if os.name == 'nt' else ''  # Colabでは日本語フォントがインストールされてないので注意
  ,'figure.figsize' : [7.0, 3.0]
  ,'figure.dpi' : 300
  ,'savefig.dpi' : 300
  ,'figure.titlesize' : 'large'
  ,'legend.fontsize' : 'small'
  ,'axes.labelsize' : 'medium'
  ,'xtick.labelsize' : 'small'
  ,'ytick.labelsize' : 'small'
})


plt.rcParams["font.size"] = 18
HOP = 1000
BACKGROUND_COLOR = "rgb(17,17,17)"
COLOR = "#fff"


def main():
    file_uploader = st.file_uploader("Upload file", type=['mp3', 'wav'])
    if file_uploader:
        wav, sr = librosa.load(file_uploader, sr=None)
        wav_seconds = int(len(wav)/sr)    

        fig, ax = plt.subplots()
        librosa.display.waveshow(wav,sr=sr, x_axis="time", ax=ax)

        st.audio(file_uploader)#音を流す

        st.pyplot(fig)


        # fig = go.Figure()
        # x_wav = np.arange(len(wav)) / sr
        # fig.add_trace(go.Scatter(y=wav[::HOP], name="wav"))
        # fig.update_layout(title="sound waveform",
        #                   xaxis=dict(
        #                       tickmode='array',
        #                       tickvals=[
        #                           1, int(len(wav[::HOP])/2), len(wav[::HOP])],
        #                       ticktext=[str(0), str(
        #                           int(wav_seconds/2)), str(wav_seconds)],
        #                       title="time(s)"
        #                   ))
        # st.plotly_chart(fig)

    # with wave.open(file, mode='rb') as wf:
    #     st.write('time(second): ', float(wf.getnframes() / wf.getframerate()))

        # print('time(second): ', float(wf.getnframes() / wf.getframerate()))

    # if file:
    #     st.audio(file)


if __name__ == '__main__':
    main()
