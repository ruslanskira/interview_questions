//calculate the average exchange rate for the last month 
public double calculateAverageRate(String targetCurrency, LocalDateTime startDate){ {{{
    double sum = 0;
    int count = 0;
    for (int i = 0; i < exchangeRates.size(); i++) {
        ExchangeRate rate = exchangeRates.get(i);
        if (rate.getDate().isAfter(startDate)) {
            sum += rate.getRate(targetCurrency);
            count++;
        }
    }
    return sum / count;
}}} 