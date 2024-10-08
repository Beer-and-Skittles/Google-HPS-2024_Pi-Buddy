PISUGAR3_ADDR = 0x57

STATUS1                 = 0x02
POWER_SUPPLY_BIT        = 7
POWER_SUPPLY_LEN        = 1
CHARGING_SWITCH_BIT     = 6
CHARGING_SWITCH_LEN     = 1
OUTPUT_SWITCH_BIT       = 5
OUTPUT_SWITCH_LEN       = 1
DEVICE_ON_WHEN_POWER_CONNECT_BIT = 4
DEVICE_ON_WHEN_POWER_CONNECT_LEN = 1
ANTIMISTAKEN_TOUCH_BIT  = 3
ANTIMISTAKEN_TOUCH_LEN  = 1
POWER_BTN_STATE_BIT     = 0
POWER_BTN_STATE_LEN     = 1

STATUS2                 = 0x03
CHIP_TEMP               = 0x04
STATUS3                 = 0x06
SW_WDT_TIMEOUT          = 0x07

CUSTOM_BTN              = 0x08
CUSTOM_BTN_BIT          = 0
CUSTOM_BTN_LEN          = 3

WRITE_PROTECTION        = 0x0B

CHARGING_PROTECTION     = 0x20
CHARGING_PROTECTION_BIT = 7
CHARGING_PROTECTION_LEN = 1

VOLTAGE_HIGH            = 0x22
VOLTAGE_LOW             = 0x23
POWER_PROPORTION        = 0x2A

RTC_YEAR                = 0x31 
RTC_MONTH               = 0x32
RTC_DAY                 = 0x33
RTC_WEEKDAY             = 0x34
RTC_HOUR                = 0x35
RTC_MINUTE              = 0x36
RTC_SECOND              = 0x37