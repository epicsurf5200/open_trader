if [ ! -d "open_trader" ]; then
    echo "Creating virtual environment..."
    if python3 -m venv open_trader; then
        echo "Virtual environment created."
    else
        echo "Failed to create virtual environment."
        return 1
    fi
fi

echo "Activating virtual environment..."
if ! source open_trader/bin/activate; then
    echo "Failed to activate virtual environment."
    return 1
fi

echo "Installing pip wheels..."
if ! pip install --no-index --no-deps packages/wheelhouse/*.whl; then
    echo "Failed to install pip wheels."
    return 1
fi

echo "Setting environment variables..."
if ! source ./env.sh; then
    echo "Failed to set environment variables."
    return 1
fi

echo "OpenTrader Installed!"