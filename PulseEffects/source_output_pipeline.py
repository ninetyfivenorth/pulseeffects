# -*- coding: utf-8 -*-

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
from PulseEffects.pipeline_base import PipelineBase


Gst.init(None)


class SourceOutputPipeline(PipelineBase):

    def __init__(self, sampling_rate):
        PipelineBase.__init__(self, sampling_rate)

        self.build_pipeline()

    def build_pipeline(self):
        self.pipeline.add(self.audio_src)
        self.pipeline.add(self.source_caps)
        self.pipeline.add(self.limiter_input_level)
        self.pipeline.add(self.limiter)
        self.pipeline.add(self.limiter_output_level)
        self.pipeline.add(self.compressor)
        self.pipeline.add(self.compressor_output_level)
        self.pipeline.add(self.reverb_bin)
        self.pipeline.add(self.highpass_bin)
        self.pipeline.add(self.lowpass_bin)
        self.pipeline.add(self.equalizer_bin)
        self.pipeline.add(self.spectrum)
        self.pipeline.add(self.output_limiter)
        self.pipeline.add(self.audio_sink)

        self.audio_src.link(self.source_caps)
        self.source_caps.link(self.limiter_input_level)
        self.limiter_input_level.link(self.limiter)
        self.limiter.link(self.limiter_output_level)
        self.limiter_output_level.link(self.compressor)
        self.compressor.link(self.compressor_output_level)
        self.compressor_output_level.link(self.reverb_bin)
        self.reverb_bin.link(self.highpass_bin)
        self.highpass_bin.link(self.lowpass_bin)
        self.lowpass_bin.link(self.equalizer_bin)
        self.equalizer_bin.link(self.spectrum)
        self.spectrum.link(self.output_limiter)
        self.output_limiter.link(self.audio_sink)