# 200312 13:32
# Chapter02-03
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

# 클래스 선언
class Car(object):
    '''
    Car Class
    Author : Me
    Date : 2019.11.08
    Description : Class, Static, Instance Method
    '''

    # Class Variable 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # self : 객체의 고유한 속성 값 사용
    # self 가 들어가 있으면 일단은 인스턴스 메소드라고 이해하면 됩니다.
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
        
    # Instance Method
    # price라는 아예 만들어서 반환을 하죠
    # 이때 self가 있겠죠 왜? 어떤 차의 가격을 반환해야 하는지 알아야 하니까 인스턴스 메소드를 써야 하겠죠
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    # 물가가 상승된 다음 가격 반환하는 메소드도 미리 만들죠
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    # 클래스 메소드를 만들어서 비율을 변경해보자
    # 첫번째 인자로 cls를 받는다.
    # cls가 Car 입니다
    # 공통적인 클래스 변수들을 컨트롤하고 값을 수정하거나 읽어오거나 read하거나 write할 때
    # 클래스 메소드를 명시적으로 쓰는겁니다. 그러면 가독성도 좋고 어? 클래스 메소드네. 클래스변수를
    # 수정하거나. 얘는 클래스 변수가져다가 뭐할려는거지? 그리고 클래스 변수는 모두가 참조하기 때문에 중요
    # 그래서 집중해서 볼 수 있게
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        return 'Succeed! price increased.'

    # Static Method
    # 스테이틱 메소드는 아무것도 전달받지 않습니다.
    # 자주쓰이지는 않지만 전체적으로 아우를 수 있는 메소드를 만들고 싶을때
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}.'.format(inst._company)
        return 'Sorry. This car is not Bmw.'
    
    
# 자동차 인스턴스    
car1 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car2 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 기본 정보
print(car1)
print(car2)
print()

# 전체 정보
car1.detail_info()
car2.detail_info()
print()

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print()

# 가격 인상(클래스 메소드 미사용)
# 직접 접근해서 수정하는 거는 좋지 않아요
Car.price_per_raise = 1.2

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()


# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)
print()

# 가격 정보(인상 후 : 클래스메소드)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# Bmw 여부(스테이틱 메소드 미사용)
def is_bmw(inst):
    if inst._company == 'Bmw':
        return 'OK! This car is {}.'.format(inst._company)
    return 'Sorry. This car is not Bmw.'

# 별도의 메소드 작성 후 호출
print(is_bmw(car1))
print(is_bmw(car2))
print()

# Bmw 여부(스테이틱 메소드 사용)
# 되게 유연해서 클래스로 호출해도 됨 Car.
# 클래스로 호출(스테이틱)
print('Static : ', Car.is_bmw(car1))
print('Static : ', Car.is_bmw(car2))
print()

# 인스턴스로 호출(스테이틱)
print('Static : ', car1.is_bmw(car1))
print('Static : ', car2.is_bmw(car2))