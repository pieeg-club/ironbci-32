import argparse
import logging
import time

import pyqtgraph as pg
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, DetrendOperations
from pyqtgraph.Qt import QtWidgets, QtCore


class Graph:
    def __init__(self, board_shim):
        self.board_id = board_shim.get_board_id()
        self.board_shim = board_shim
        self.exg_channels = BoardShim.get_exg_channels(self.board_id)
        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)
        self.update_speed_ms = 50
        self.window_size = 4
        self.num_points = self.window_size * self.sampling_rate

        self.app = QtWidgets.QApplication([])
        self.win = pg.GraphicsLayoutWidget()
        self.win.setWindowTitle('BrainFlow - Single Channel Plot')
        self.win.resize(800, 400)
        self.win.show()

        self._init_timeseries()

        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(self.update_speed_ms)

        QtWidgets.QApplication.instance().exec()

    def _init_timeseries(self):
        self.plot = self.win.addPlot(title='TimeSeries Plot - Channel 1')
        self.plot.showAxis('left', True)
        self.plot.setMenuEnabled('left', False)
        self.plot.showAxis('bottom', False)
        self.plot.setMenuEnabled('bottom', False)
        self.curve = self.plot.plot()

    def update(self):
        data = self.board_shim.get_current_board_data(self.num_points)
        channel = self.exg_channels[0]  # Only the first channel

        DataFilter.detrend(data[channel], DetrendOperations.CONSTANT.value)
        DataFilter.perform_bandpass(data[channel], self.sampling_rate, 3.0, 45.0, 2,
                                    FilterTypes.BUTTERWORTH.value, 0)
        DataFilter.perform_bandstop(data[channel], self.sampling_rate, 48.0, 52.0, 2,
                                    FilterTypes.BUTTERWORTH.value, 0)
        DataFilter.perform_bandstop(data[channel], self.sampling_rate, 58.0, 62.0, 2,
                                    FilterTypes.BUTTERWORTH.value, 0)

        self.curve.setData(data[channel].tolist())
        self.app.processEvents()


def main():
    BoardShim.enable_dev_board_logger()
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int, default=0)
    parser.add_argument('--ip-port', type=int, default=0)
    parser.add_argument('--ip-protocol', type=int, default=0)
    parser.add_argument('--ip-address', type=str, default='')
    parser.add_argument('--serial-port', type=str, default='COM3')
    parser.add_argument('--mac-address', type=str, default='')
    parser.add_argument('--other-info', type=str, default='')
    parser.add_argument('--streamer-params', type=str, default='')
    parser.add_argument('--serial-number', type=str, default='')
    parser.add_argument('--board-id', type=int, default=BoardIds.FREEEEG32_BOARD)
    parser.add_argument('--file', type=str, default='')
    args = parser.parse_args()

    params = BrainFlowInputParams()
    params.ip_port = args.ip_port
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address
    params.other_info = args.other_info
    params.serial_number = args.serial_number
    params.ip_address = args.ip_address
    params.ip_protocol = args.ip_protocol
    params.timeout = args.timeout
    params.file = args.file

    try:
        board_shim = BoardShim(args.board_id, params)
        board_shim.prepare_session()
        board_shim.start_stream(450000, args.streamer_params)
        Graph(board_shim)
    except BaseException:
        logging.warning('Exception', exc_info=True)
    finally:
        logging.info('End')
        if board_shim.is_prepared():
            logging.info('Releasing session')
            board_shim.release_session()


if __name__ == '__main__':
    main()
