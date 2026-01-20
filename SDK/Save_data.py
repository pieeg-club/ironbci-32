from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
import time
import pandas as pd

# Enable logging (optional)
BoardShim.enable_dev_board_logger()

# Set up BrainFlow parameters
params = BrainFlowInputParams()
params.serial_port = "COM3"  # change if needed

board = BoardShim(BoardIds.IRONBBCI_32_BOARD, params)

print("Board initialized")

try:
    # Prepare and start streaming
    board.prepare_session()
    board.start_stream()
    print("Streaming started. Collecting data for 10 seconds...")

    time.sleep(10)

    # Stop stream and get data
    board.stop_stream()
    data = board.get_board_data()
    print(f"Raw data shape: {data.shape}")

    # Get EEG (EXG) channels only
    eeg_channels = BoardShim.get_exg_channels(BoardIds.FREEEEG32_BOARD)
    eeg_data = data[eeg_channels, :]

    # Transpose: rows = samples, columns = channels
    eeg_data = eeg_data.T

    # Create column names
    columns = [f"Ch{i+1}" for i in range(len(eeg_channels))]

    # Create DataFrame
    df = pd.DataFrame(eeg_data, columns=columns)

    # Save to Excel
    output_file = "eeg_32ch_10s.xlsx"
    df.to_excel(output_file, index=False)

    print(f"Data saved to {output_file}")
    print("Final shape (rows=samples, cols=channels):", df.shape)

finally:
    board.release_session()
    print("Session released.")




    

         
