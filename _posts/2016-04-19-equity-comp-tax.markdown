---
layout: post
title:  "On Equity Compensation Tax"
date:   2016-04-19 22:12:22 -0800
categories: stock tax
---
It's that time of the year - yes I'm talking about tax.

Unlike previous years I learned a lot more about tax from this year's return, as I joined a start-up 1.5 years ago and things are acutely different from before. Most of the tax work you can still do with software (I used TurboTax) but you have to be mentally and financially prepared for what might happen.

## Startup Job Compensation
We all know the compensation structure for startup jobs usually consists of `cash` + `equity`. Cash part tends to be tight and they make it up with equity. Cash is always easy. But what about equity?

Likely `Equity` comes in two forms as fas as I know: `Stock option` or `RSU`.

 - `Stock option` represents the the possibility to purchase certain amount of company shares at certain price (usually agreed upon in job offer letter).
 - `RSU` is for the company to directly issue shares to you. You get it for free no action required.

Both have a vesting schedule. Silicon Valley has universally adopted 1-year-cliff + month by month schedule, meaning you get 25% of it (whatever it is) after a year, and get a fair share per month going forward. E.g. you are promised with 4,000 RSU shares. Before you have stayed a year with the company you get nothing. When you make a year through, you will be given 1000 shares. Then for each month to follow, you get about 83 shares till it's fully vested. Similarly if it's stock options, after a year you will be able to purchase 1000 shares, and so on.

## Glossary
Before deep diving into all the details, let's get the terms straight:

 - `strike price`: a price that you and your employer both agreed upon at which to purchase stock options. the later stage you join the high this will be.
 - `exercise`: when you purchase stock options at strike price.
 - `early exercise`: purchase stock options before they are vested.
 - `exercise price`: strike price
 - `spread`:  market price - strike price
 - `ISO`: Incentive stock options. Has some tax benefits. More to follow.
 - `NSO`: Nonstatutory stock options. Taxed as income.
 - `Fair Market Value`:
 - `AMT`: Alternative Minimum Tax. It's meant for people to avoid paying too little tax. Its tax rates are: 26% for < taxable income of $185,400; 28% if over (2015). Numbers subject to change. See 6251 instructions. 


## Tax difference:
 - `ISO`: No tax when exercised but it may trigger AMT. When sold, (Market price - FMV) is taxed as long-term capital gain.
 - `NSO`: When exercised, spread is taxed at income tax rate


## Case study:
One or multiple cases below might happtn to you:

 - You start working at the red-hot startup
   - Granted options -> Vest -> Early Exercise (pay a lot of cash) -> Tax return triggers AMT (pay a lot of cash), or
   - Granted options -> Vest -> Do nothing just wait.
   - Granted RSUs -> Vest -> Do nothing just wait.
 - A: Company goes public and you are still with the it.
   - Company IPO -> Sell them to market. Pay long-term capital gain if ISO. Or
   - Company IPO but trading lower than your strike price -> If you sell you lose money. Or
 - B: Company nevers goes public
   - This really sucks as you dont get your money back. You may get the your early-exercise expense back from the company however.
 - C: Somehow you decided to leave the company and but it isn't public yet. For the remaining RSU you can't argue about it. You just get the f out the door and forget about it. For options, you are given the opportunity to exercise the vested ones but you may or may not have exercised all of them. Should you exercise the remaining? If yes how much to exercise? There's no simple answer - it depends on if you expect the company to have an exit soon, how financially comfortable you are with exercising, and if there is other financial opportunities for you to invest in. Ask friends or financial advisor to get some input.
- Company goes public and you are still with the company. You can choose to sell your shares or hold. Options and RSUs are not that much different except that options might be taxed as long-term capital gain.
- You early exercise options. This seems common among high-growth startups. There might be a few benefits of early exercising your options:
  - You exercise the options at a relatively lower price
  - If you hold it 1 year and 2 years you only pay long-term capital gain which is a lot lower than income tax

There are a few catches as well:

  - You pay a large amount of cash upfront for future options (depends on your strike price of course)
  - It may trigger AMT, which is another nontrivial quantity of cash
  - If you terminate your job before what you early exercised is vested, the AMT tax won't be returned

Let's go through a hypothetical example:

 - John joined hyper-growth company ABC (no not alphabet) and was granted 20,000 shares of stock options at strike price of $6.
 - 6 month in he was given the chance to early exercise. He did so with 10,000 shares and he paid $60k. FMV of this moment was $16.
 - Assume he made about $100,000 cash last year. Then he needs pay ($100,000 `salary` + $100,000 `capital gain`) * 0.28 `AMT tax rate` = $56,000 - `tax deducted from paycheck` to IRS.

Yes you may not have that much saving and you may not have $80k to early exercise that much. But if you do, be aware you have to pay tax on top of it.

## When X Do Y

 - Submit Election Form (83b) to IRS within 30 days of early exercise.
 - When you leave the company you are given certain time period (usually 30 days) to exercise vested shares.
 - When you file tax return your find you are not able to handle the large amount of tax you owe to IRS, ask for payment installment.

## Lesson learned

 - Lesson learned: ISO is supposed to receive a favorable tax treatment in the longer term but there is a catch. To early exercise, not only you pay a large amount of cash upfront (depends on the strike price and amount of shares), but also you need pay a significant amount of AMT tax. So be prepared (I wasn't).

Best of luck with your startup equity!

## Further reading:

* [Things you should know about stock options before negotiating an offer](http://jvns.ca/blog/2015/12/30/do-the-math-on-your-stock-options/)
* [The Open Guide to Equity Compensation](https://github.com/jlevy/og-equity-compensation)
