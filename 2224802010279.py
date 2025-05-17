mssv = "2224802010279"

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'eurus'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = "5432"


POSTGRES_DB_NAME = '2224802010279'


from sqlalchemy import create_engine, Column, String,Integer,ForeignKey,or_, and_, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import select 

DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Dinh nghia Table Model

class KhachHang(Base):
    __tablename__ = 'khachhang'
    MAKH = Column(String, primary_key=True)
    TENKH = Column(String)
    DIACHI = Column(String)
    LOAIKH = Column(String)
    dien_thoais= relationship("DienThoai", back_populates="khach_hang")

    def __repr__(self):
        return f"<KhachHang(MAKH='{self.MAKH}',TENKH='{self.TENKH}',LOAIKH='{self.LOAIKH}')"
    
class DienThoai(Base):
    __tablename__ = 'dienthoai'
    SODT = Column(String, primary_key=True)
    MAKH = Column(String, ForeignKey('khachhang.MAKH'))
    LOAIDT = Column(String)
    SOHD=Column(String)

    khach_hang=relationship("KhachHang", back_populates="dien_thoais")
    dang_kys = relationship("DangKy", back_populates="dien_thoai")

    def __repr__(self):
        return f"<DienThoai(SODT='{self.SODT}',MAKH='{self.MAKH}')>"
class DichVu(Base):
    __tablename__='dichvu'
    MADV = Column(String, primary_key=True)
    TENDV = Column(String)

    dang_kys = relationship("DangKy", back_populates="dich_vu")
    
    def __repr__(self):
        return f"<DichVu(MADV='{self.MADV}', TENDV='{self.TENDV}')>"


class DangKy(Base):
    __tablename__ = 'dangky'
    MADV = Column(String, ForeignKey('dichvu.MADV'), primary_key=True)
    SODT = Column(String, ForeignKey('dienthoai.SODT'), primary_key=True)

    dien_thoai = relationship("DienThoai", back_populates="dang_kys")
    dich_vu = relationship("DichVu", back_populates="dang_kys")

    def __repr__(self):
        return f"<DangKy(MADV='{self.MADV}', SODT='{self.SODT}')>"


# HAM TAO BANG

def create_and_populate_db():
    Base.metadata.create_all(engine)

    num_rows_to_insert = 5
    print(f"MSSV: {mssv}, Yeu cau nhap {num_rows_to_insert} dong moi bang. ")

    # Xóa dữ liệu cũ trước khi nhập mới
    session.query(DangKy).delete()
    session.query(DienThoai).delete()
    session.query(DichVu).delete()
    session.query(KhachHang).delete()
    session.commit()

    khach_hang_data = [
        {'MAKH': 'KH001', 'TENKH': 'Nguyễn Văn An', 'DIACHI': '123 Đường ABC, Quận 1, TP.HCM', 'LOAIKH': 'Cá nhân'},
        {'MAKH': 'KH002', 'TENKH': 'Công ty TNHH XYZ', 'DIACHI': 'Lô A1, KCN Sóng Thần, Bình Dương', 'LOAIKH': 'Doanh nghiệp'},
        {'MAKH': 'KH003', 'TENKH': 'Trần Thị Bích Anh', 'DIACHI': '456 Đường DEF, Quận Thủ Đức, TP.HCM', 'LOAIKH': 'Cá nhân'},
        {'MAKH': 'KH004', 'TENKH': 'Doanh nghiệp tư nhân Hoàng Long', 'DIACHI': '789 Đường GHI, Dĩ An, Bình Dương', 'LOAIKH': 'Doanh nghiệp'},
        {'MAKH': 'KH005', 'TENKH': 'Lê Văn Cường', 'DIACHI': '101 Đường KLM, Quận 3, TP.HCM', 'LOAIKH': 'Cá nhân'},
    ]
    dien_thoai_data = [
        {'SODT': '0901112221', 'MAKH': 'KH001', 'LOAIDT': 'Vô tuyến', 'SOHD': 'HD001'},
        {'SODT': '0901112222', 'MAKH': 'KH001', 'LOAIDT': 'Dây cáp', 'SOHD': 'HD002'},
        {'SODT': '0913334441', 'MAKH': 'KH002', 'LOAIDT': 'Vô tuyến', 'SOHD': 'HD003'},
        {'SODT': '0985556661', 'MAKH': 'KH003', 'LOAIDT': 'Vô tuyến', 'SOHD': 'HD004'},
        {'SODT': '0907778881', 'MAKH': 'KH004', 'LOAIDT': 'Dây cáp', 'SOHD': 'HD005'},
    ]
    dich_vu_data = [
        {'MADV': 'DV001', 'TENDV': 'SMS'},
        {'MADV': 'DV002', 'TENDV': 'funring'},
        {'MADV': 'DV003', 'TENDV': 'Data 4G'},
        {'MADV': 'DV004', 'TENDV': 'Call Forwarding'},
        {'MADV': 'DV005', 'TENDV': 'Voice Mail'},
    ]
    dang_ky_data = [
        {'MADV': 'DV001', 'SODT': '0901112221'}, # SMS cho An
        {'MADV': 'DV002', 'SODT': '0901112221'}, # funring cho An
        {'MADV': 'DV001', 'SODT': '0913334441'}, # SMS cho Cty XYZ
        {'MADV': 'DV001', 'SODT': '0985556661'}, # SMS cho Anh
        {'MADV': 'DV002', 'SODT': '0907778881'}, # funring cho DN Hoang Long
    ]

    for data in khach_hang_data[:num_rows_to_insert]:
        session.add(KhachHang(**data))
    for data in dien_thoai_data[:num_rows_to_insert]:
        session.add(DienThoai(**data))
    for data in dich_vu_data[:num_rows_to_insert]:
        session.add(DichVu(**data))
    
    added_dangky_count = 0
    for data in dang_ky_data:
        if added_dangky_count >= num_rows_to_insert:
            break
        sodt_exists = any(dt['SODT'] == data['SODT'] for dt in dien_thoai_data[:num_rows_to_insert])
        madv_exists = any(dv['MADV'] == data['MADV'] for dv in dich_vu_data[:num_rows_to_insert])
        
        if sodt_exists and madv_exists:
            session.add(DangKy(**data))
            added_dangky_count +=1
            
    session.commit()
    print(f"Đã nhập {session.query(KhachHang).count()} dòng vào bảng KHACHHANG.")
    print(f"Đã nhập {session.query(DienThoai).count()} dòng vào bảng DIENTHOAI.")
    print(f"Đã nhập {session.query(DichVu).count()} dòng vào bảng DICHVU.")
    print(f"Đã nhập {session.query(DangKy).count()} dòng vào bảng DANGKY .")
    return num_rows_to_insert


# Cau 2: Thuc hien cac truy van
# a. Hãy liệt kê các dịch vụ cho khách hàng cá nhân.

def query_a():
    print("\n--- a. Dịch vụ cho từng khách hàng cá nhân ---")
    results = session.query(
        KhachHang.TENKH.label("TenKhachHang"),
        DienThoai.SODT.label("SoDienThoai"),
        DichVu.TENDV.label("TenDichVu")
    ) \
    .join(DienThoai, KhachHang.MAKH == DienThoai.MAKH) \
    .join(DangKy, DienThoai.SODT == DangKy.SODT) \
    .join(DichVu, DangKy.MADV == DichVu.MADV) \
    .filter(KhachHang.LOAIKH == 'Cá nhân') \
    .order_by(KhachHang.TENKH, DichVu.TENDV) \
    .all()
    if results:
        for row in results:
            print(f"Khách hàng: {row.TenKhachHang}, SĐT: {row.SoDienThoai}, Dịch vụ: {row.TenDichVu}")
    else:
        print("Không có khách hàng cá nhân nào đăng ký dịch vụ.")


# b. Hãy liệt kê số điện thoại khách hàng đăng ký dịch vụ SMS.

def query_b():
    print("\n--- b. Chi tiết số điện thoại đăng ký dịch vụ SMS ---")
    results = session.query(
        DienThoai.SODT.label("SoDienThoai"),
        KhachHang.TENKH.label("TenKhachHang"),
        DichVu.TENDV.label("TenDichVu")
    ) \
    .join(DangKy, DienThoai.SODT == DangKy.SODT) \
    .join(DichVu, DangKy.MADV == DichVu.MADV) \
    .join(KhachHang, DienThoai.MAKH == KhachHang.MAKH) \
    .filter(DichVu.TENDV == 'SMS') \
    .order_by(DienThoai.SODT) \
    .all()
    if results:
        for row in results:
            print(f"SĐT: {row.SoDienThoai}, Khách hàng: {row.TenKhachHang}, Dịch vụ: {row.TenDichVu}")
    else:
        print("Không có số điện thoại nào đăng ký dịch vụ SMS.")

# c. Hãy liệt kê các dịch vụ SMS cho khách hàng cá nhân hoặc doanh nghiệp.
def query_c():
    print("\n--- c. Dịch vụ SMS cho khách hàng cá nhân hoặc doanh nghiệp ---")
    results = session.query(KhachHang.TENKH, KhachHang.LOAIKH, DichVu.TENDV) \
        .join(DienThoai, KhachHang.MAKH == DienThoai.MAKH) \
        .join(DangKy, DienThoai.SODT == DangKy.SODT) \
        .join(DichVu, DangKy.MADV == DichVu.MADV) \
        .filter(DichVu.TENDV == 'SMS') \
        .filter(or_(KhachHang.LOAIKH == 'Cá nhân', KhachHang.LOAIKH == 'Doanh nghiệp')) \
        .distinct() \
        .all()
    if results:
        print(f"Dịch vụ 'SMS' được sử dụng bởi các khách hàng sau (Cá nhân hoặc Doanh nghiệp):")
        for kh_ten, kh_loai, dv_ten in results:
            print(f"- Khách hàng: {kh_ten}, Loại: {kh_loai}, Dịch vụ: {dv_ten}")
    else:
        print("Không tìm thấy dịch vụ SMS nào được đăng ký bởi khách hàng cá nhân hoặc doanh nghiệp.")

# d. Cho biết các dịch vụ do khách hàng tên Anh hoặc An đăng ký.
def query_d():
    print("\n--- d. Dịch vụ do khách hàng tên Anh hoặc An đăng ký ---")
    results = session.query(DichVu.TENDV.label("TenDichVu"), KhachHang.TENKH.label("TenKhachHang")) \
        .join(DangKy, DichVu.MADV == DangKy.MADV) \
        .join(DienThoai, DangKy.SODT == DienThoai.SODT) \
        .join(KhachHang, DienThoai.MAKH == KhachHang.MAKH) \
        .filter(or_(KhachHang.TENKH.like('%Anh%'), KhachHang.TENKH.like('%An%'))) \
        .distinct() \
        .all()
    for row in results:
        print(f"Dịch vụ: {row.TenDichVu} (Khách hàng: {row.TenKhachHang})")

# e. Cho biết các dịch vụ do Doanh nghiệp ở Bình Dương đăng ký.
def query_e():
    print("\n--- e. Dịch vụ do Doanh nghiệp ở Bình Dương đăng ký ---")
    results = session.query(DichVu.TENDV.label("TenDichVu"), KhachHang.TENKH.label("TenDoanhNghiep")) \
        .join(DangKy, DichVu.MADV == DangKy.MADV) \
        .join(DienThoai, DangKy.SODT == DienThoai.SODT) \
        .join(KhachHang, DienThoai.MAKH == KhachHang.MAKH) \
        .filter(KhachHang.LOAIKH == 'Doanh nghiệp') \
        .filter(KhachHang.DIACHI.like('%Bình Dương%')) \
        .distinct() \
        .all()
    for row in results:
        print(f"Dịch vụ: {row.TenDichVu} (Doanh nghiệp: {row.TenDoanhNghiep})")

# f. Cho biết thông tin khách hàng đăng ký cả hai dịch vụ là funring và SMS.
def query_f():
    print("\n--- f. Khách hàng đăng ký cả funring và SMS ---")
    subquery_funring = select(DienThoai.MAKH).join(DangKy, DienThoai.SODT == DangKy.SODT) \
        .join(DichVu, DangKy.MADV == DichVu.MADV) \
        .filter(DichVu.TENDV == 'funring').distinct()

    subquery_sms = select(DienThoai.MAKH).join(DangKy, DienThoai.SODT == DangKy.SODT) \
        .join(DichVu, DangKy.MADV == DichVu.MADV) \
        .filter(DichVu.TENDV == 'SMS').distinct()

    results = session.query(KhachHang.TENKH, KhachHang.DIACHI, KhachHang.LOAIKH) \
        .filter(KhachHang.MAKH.in_(subquery_funring)) \
        .filter(KhachHang.MAKH.in_(subquery_sms)) \
        .all()
    
    for kh in results:
        print(f"Tên: {kh.TENKH}, Địa chỉ: {kh.DIACHI}, Loại: {kh.LOAIKH}")


# Ham main thuc thi
if __name__ == "__main__":
    print(f"Sử dụng PostgreSQL database: {POSTGRES_DB_NAME} trên host {POSTGRES_HOST}")

    
    # Câu 1: Tạo CSDL và nhập liệu
    print("\n--- Câu 1: Tạo CSDL (bảng) và Nhập liệu ---")
    num_rows = create_and_populate_db()
    print(f"Đã tạo/kiểm tra các bảng và nhập liệu.")

    # Câu 2: Thực hiện các truy vấn
    print("\n--- Câu 2: Thực hiện các truy vấn ---")
    query_a()
    query_b()
    query_c()
    query_d()
    query_e()
    query_f()

    session.close()
    print("\nHoàn thành Lab 6.1 với PostgreSQL.")
  
 
   