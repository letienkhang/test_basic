class ParityPriceLocators:

    FIRST_PRODUCT = '//div[contains(@class, "grid gap-x-3 gap-y-5 px-4 md:px-0 md:gap-y-10 grid-cols-2 xmd:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 mb-5 md:mb-4")]/div[1]'
    INPUT_SEARCH_BUTTON = '//input[contains(@class, "input__m") and contains(@class, "input--default")]'
    INPUT_SEARCH = '//input[contains(@class, "input__l") and contains(@class, "input--default")]'
    GET_PRICE_PRODUCT_ELEMENT = "//div[contains(@class, 'name-and-price_price_wrapper')]/p[contains(@class, 'price-element')]"
    COMPARE_AT_PRICE_ELEMENT = "(//p[contains(@class, 'compare-at-price-element')])[1]"
    DISCOUNT_TAG_ELEMENT = "(//span[contains(@class, 'text-yd-label-5')])[1]"
    CODE_PRODUCT_ELEMENT = "//span[contains(@class, 'uppercase') and contains(@class, 'text-[#292929]') and contains(@class, 'text-[14px]') and contains(@class, 'mr-[4px]')]"
    CLEAR_TEXT_SEARCH_ELEMENT = "//button[@class='hover:scale-110 active:scale-100 inline-block focus-visible:outline-none visited:outline-none opacity-60 group-hover:opacity-100 transition-all duration-200 hover:duration-75 undefined']"
    COMPARE_AT_PRICE_ELEMENT =  "//p[contains(@class, 'compare-at-price-element')]"
    DISCOUNT_ELEMENT = "//span[contains(@class, 'text-yd-label-5') and contains(@class, 'text-current')]"
    POPUP =  "//div[@class='ins-slider-page ins-element-wrap ins-element-sub-frame ins-active-slide']"
    POPUP_CLOSE_BUTTON =  "//div[@id='wrap-close-button-1454703513202']"