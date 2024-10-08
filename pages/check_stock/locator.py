
class CheckStockLocators:
 ADD_TO_CART = "//button[contains(@class, 'product-call-to-action_add-cart_button') and .//span[text()='Thêm vào giỏ']]"
 QUALITY_PLUS_BUTTON= "//button[@class='product-quantity-update-tool_button__dMhNl product-quantity-update-tool_button_right__MHn0c product-quantity-update-tool_button-normal__YS_yD  undefined']"
 BUY_NOW_BUTTON = "//button[contains(@class, 'btn-extra-large') and contains(@class, 'product-call-to-action_buy-now_button') and .//span[text()='Mua ngay']]"
 CHECKOUT_BUTTON = "//button[@class=' btn btn-extra-large btn-solid btn-solid-primary btn-solid-3d-primary w-full mt-7']"
 DATANAME = "Test Đơn web"
 DATAPHONE = "0900000001"
 DATA_ADDRESS = "90 Le Loi"
 ADDRESS_CUS = "//div[@class = 'w-full relative select-city-district-ward !rounded-[4px] !border-yd-gray-50 text-yd-typo-title']"
 CHOOSE_CITY = "//div[@class= 'font-regular text-yd-label-4 text-yd-typo-label']"
 ADDRESS_CITY = "//input[@class= ' input__m input--default pl-12 pr-4  w-full w-full h-11 !pl-9 !rounded-none !border-t-0 !border-r-0 !border-l-0 truncate']"
 FILLNAME_CUSTOMER = "//input[@class=' input__xl input--default pl-12 pr-4  w-full h-[52px] !pr-3 !pl-[42px] rounded-[4px] placeholder:text-yd-gray-100 border-yd-gray-50 truncate'][@name='name']"
 FILLPHONECUSTOMER = "//input[@class=' input__xl input--default pl-12 pr-4  w-full h-[52px] !pr-3 !pl-[42px] rounded-[4px] placeholder:text-yd-gray-100 border-yd-gray-50 truncate'][@name='phone']"
 DETAIL_CUSTOMER = "//input[@name='address'][@class=' input__xl input--default pl-4 pr-4  w-full h-[52px] rounded-[4px] placeholder:text-yd-gray-100 border-yd-gray-50 truncate']"
 NOTE_ORDER = "//input[@class=' input__xl input--default pl-12 pr-4  w-full h-[52px] !pr-3 !pl-[42px] rounded-[4px] placeholder:text-yd-gray-100 border-yd-gray-50 truncate'][@name= 'note']"
 PAYMENT_BUTTON = "//button[@class= ' btn btn-solid btn-solid-primary btn-solid-3d-primary w-full h-[48px]']"