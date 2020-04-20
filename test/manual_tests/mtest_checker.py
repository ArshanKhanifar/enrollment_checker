from src.checker import Checker

if __name__ == '__main__':
    data = Checker().check_availability('under', '1205', 'MUSIC', '140')
    print(data)
