from app import app
from app.GPIOSwitcher import GPIOSwitcher

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        GPIOSwitcher.cleanup()

