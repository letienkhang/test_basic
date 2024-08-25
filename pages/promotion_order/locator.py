
class ProductDiscountLocators:
    LOGIN_WITH_YODY_ID_BUTTON = "//ul[@class='pf-c-login__main-footer-links kc-social-links ']"
    INPUT_USERNAME = "//input[@class='pf-c-form-control'][@name='username']"
    USER_PASS_INPUT = "//input[@class='pf-c-form-control'][@name='password']"
    LOGIN_BUTTON = "//div[@class='form-group']//input[@class ='pf-c-button pf-m-primary pf-m-block btn-lg'][@name='login']"
    ITEM_MENU_PROMOTION = "//div[@class='ant-menu-submenu-title']//span[@class='ant-menu-title-content']//div[text()='Khuyến mại']"
    ITEM_MENU_WEBAPP = "//div[@class='ant-menu-submenu-title']//span[@class='ant-menu-title-content']//div[text()='Web/App']"
    ITEM_MENU_MANAGE_THE_PROMOTION = "//li[@role='menuitem' and @tabindex='-1']//a[@title='Quản lý chương trình KM']"
    ITEM_MENU_MANAGE_SETTING_APP = "//li[@role='menuitem' and @tabindex='-1']//a[@title='Cấu hình']"
    CHOOSE_ECOM_ADMON = "//td[contains(@class, 'ant-table-cell ant-table-cell-fix-left ant-table-cell-fix-left-last')]//strong[contains(text(), 'Ecom admin')]"
    CREATE_PROMOTION = "//button[@class='ant-btn ant-btn-lg ant-btn-outline ant-btn-primary']"
    NAME_PROMOTION_INPUT = "//div[@class='ant-form-item-control-input-content']//input[@class='ant-input']"
    OPTION_PROMOTION_BUTTON = "//div[@class='ant-select-selector']//span[@class='ant-select-selection-search']"
    TYPE_PROMOTION_DROPDOWN = "//div[@class='ant-select ant-select-single ant-select-show-arrow']"
    CHOOSE_ITEM_TYPE_DROPDOWN = "//div[@title='Chương trình MKT trong tháng']"
    CONTENT_PROMOTION_INPUT = "//textarea[@placeholder='Nhập nội dung chương trình khuyến mại']"
    CHOOSE_DUE_DATE = "(//input[@placeholder='Chọn ngày'])[2]"
    PICKER_NEXT_BUTTON = " //button[@class='ant-picker-header-next-btn']"
    DUE_DATE_NEXT_MONTH = "//div[@class='ant-picker-cell-inner' and text()='12']"
    OK_DUE_DATE_BUTTON = "//button[@class='ant-btn ant-btn-primary ant-btn-sm']//span[text()='Ok']"
    CREATE_NEW_ITEM_BUTTON = "//button[@class='ant-btn ant-btn-sm ant-btn-outline ant-btn-primary']//span[text()='Tạo mới']"
    TAB_CODE_PROMOTION = "//div[@class='ant-tabs-tab']//div[@role='tab' and text()='Mã khuyến mại']"
    CHOOSE_BY_ORDER = "//div[@class='ant-col ant-col-8 promotion-type-button ' and text()='Khuyến mại theo đơn hàng']"

    # TAO CHUONG TRINH KHUYEN MAI THANH PHAN
    OPERATION_NAME_INPUT = "//div[@class='ant-form-item-control-input-content']//input[@placeholder='Nhập tên đợt phát hành']"
    SHOW_WEDSITE_CHECKBOX = "//label[@class='ant-checkbox-wrapper']//span[text()='Hiển thị CTKM trên website']/preceding-sibling::span//input[@type='checkbox']"
    VALUE_OF_PROMOTION_INPUT = "//input[@placeholder='Nhập giá trị khuyến mại']"
    SALES_CHANNEL = '(//button[@role="switch" and @aria-checked="true" and contains(@class, "ant-switch-checked")])[7]'
    SALES_CHANNEL_OPTION = '//input[@id="issue-create_prerequisite_sales_channel_names"]'
    CREATE_AREA_INPUT = '//textarea[@id="issue-create_description"]'
    PROMO_VALUE_INPUT ='//input[@id="rulevalue"]'
    SAVE_PROMO= '//button[@class="ant-btn ant-btn-sm ant-btn-outline ant-btn-primary"]//span[text()="Lưu"]'

    #edit code promo
    EDIT_ITEM_FIRST_LIST_PROMO = '//button[@class="ant-btn ant-btn-text ant-btn-icon-only ant-dropdown-trigger remove-item-icon"]'
    EDIT_ITEM_FIRST = "//li[@class='ant-dropdown-menu-item ant-dropdown-menu-item-only-child' and @role='menuitem' and @tabindex='-1']//a[contains(@href, '/admin/promotion/issues') and contains(@href, '/update')]"
    ADD_HAND_MADE_CODE = '//div[contains(@class, "card-discount-code")]//p[text()="Thêm mã thủ công"]'
    ENTER_HAND_MADE_CODE = '//input[@placeholder="Nhập số và ký tự in hoa (tối đa 30 ký tự)" and @maxlength="30"]'
    HAND_MADE_CODE_BUTTON = '//button[@class="ant-btn ant-btn-primary"]//span[text()="Thêm"]'
    CONFIRM_HAND_CODE = '//button[@class="ant-btn ant-btn-primary"]//span[text()="Xác nhận"]'
    ENABLE_HAND_CODE = '//button[@class="ant-btn ant-btn-primary"]//span[text()="Kích hoạt"]'
    CHOOSE_CODE_LINK = "//a[starts-with(@href, '/admin/promotion/issues/')]"
    SAVE_DONE = "//button[@type='button' and contains(@class, 'ant-btn') and contains(@class, 'ant-btn-primary')]//span[text()='Lưu chương trình']"

    #confirm popup
    YES_BUTTON = "//button[@type='button' and contains(@class, 'ant-btn') and contains(@class, 'ant-btn-primary')]/span[text()='Đồng ý']"
    TURN_ON_ITEM = "//button[@type='button' and @role='switch' and @aria-checked='false' and contains(@class, 'ant-switch') and @ant-click-animating='false']"

