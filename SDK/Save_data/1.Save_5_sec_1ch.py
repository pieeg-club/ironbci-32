import time
import matplotlib.pyplot as plt
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

def main():
    BoardShim.enable_dev_board_logger()

    # Set your parameters directly here for IDLE
    params = BrainFlowInputParams()
    params.serial_port = 'COM3'  # Hardcoded COM port

    # Initialize board
    board_id = BoardIds.IRONBCI_32_BOARD
    board = BoardShim(board_id, params)
    
    try:
        board.prepare_session()
        board.start_stream()
        
        print("Capturing 5 seconds of data... please wait.")
        time.sleep(5)
        
        # Get all data and stop session
        data = board.get_board_data()
        
    finally:
        # Putting this in 'finally' ensures the board releases 
        # even if the code crashes, preventing COM port busy errors.
        if board.is_prepared():
            board.stop_stream()
            board.release_session()

    # --- Plotting Logic ---
    # Get EEG channels for this specific board
    eeg_channels = BoardShim.get_eeg_channels(board_id)
    
    # Pick the first EEG channel (usually index 1 or 0 depending on board)
    first_chan = eeg_channels[0]
    eeg_data = data[first_chan]

    plt.figure(figsize=(10, 4))
    plt.plot(eeg_data, color='blue', linewidth=0.8)
    plt.title(f'IronBCI Raw Data - Channel {first_chan}')
    plt.xlabel('Samples')
    plt.ylabel('Voltage (uV)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
