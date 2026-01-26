import argparse
import time
import matplotlib.pyplot as plt
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

def main():
    BoardShim.enable_dev_board_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument('--serial-port', type=str, help='serial port', required=True)
    args = parser.parse_args()

    params = BrainFlowInputParams()
    params.serial_port = args.serial_port

    # Initialize board
    board_id = BoardIds.IRONBCI_32_BOARD
    board = BoardShim(board_id, params)
    
    board.prepare_session()
    board.start_stream()
    
    print("Capturing 5 seconds of data...")
    time.sleep(5)
    
    # Get all data and stop session
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()

    # --- Plotting Logic ---
    # Get EEG channels for this specific board
    eeg_channels = BoardShim.get_eeg_channels(board_id)
    # Pick the first EEG channel
    first_chan = eeg_channels[0]
    eeg_data = data[first_chan]

    plt.figure(figsize=(10, 4))
    plt.plot(eeg_data)
    plt.title(f'EEG Channel {first_chan} - IronBCI')
    plt.xlabel('Samples')
    plt.ylabel('Voltage (uV)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
