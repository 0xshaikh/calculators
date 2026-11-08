"use strict";
// Gold Leverage Calculator — live compute
(function(){
  const $ = (id) => document.getElementById(id);

  const bal = $("bal");
  const lot = $("lot");
  const price = $("price");
  const contract = $("contract");
  const result = $("result");
  const empty = $("empty");
  const lev = $("lev");
  const oBal = $("o-bal"), oLot = $("o-lot"), oPrice = $("o-price"),
        oPos = $("o-pos"), oOz = $("o-oz"), oNote = $("o-note");

  const STANDARD = [50, 100, 200, 300, 400, 500]; // common broker leverages

  const money = (v) =>
    "$" + v.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const qty = (v) =>
    v.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const lots = (v) =>
    v.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  function fmtLeverage(x){
    // "you need" → round UP to next whole for the ratio
    if (x >= 100) return Math.ceil(x).toLocaleString("en-US");
    if (x >= 10)  return x.toFixed(1);
    return x.toFixed(2);
  }

  function nearestStd(req){
    for (const s of STANDARD) if (s >= req) return s;
    return STANDARD[STANDARD.length - 1];
  }

  function calc(){
    const b = parseFloat(bal.value);
    const l = parseFloat(lot.value);
    const p = parseFloat(price.value);
    const ozPerLot = parseInt(contract.value, 10);

    const ok = b > 0 && l > 0 && p > 0 && ozPerLot > 0;

    if (!ok){
      result.hidden = true;
      empty.hidden = false;
      return;
    }

    const goldOz = l * ozPerLot;       // gold quantity in oz
    const posVal = goldOz * p;         // position value in $
    const req = posVal / b;            // required leverage (x:1)

    // display
    lev.textContent = (req >= 1 ? "1:" : "") + fmtLeverage(req);
    oBal.textContent = money(b);
    oLot.textContent = lots(l) + " lots";
    oPrice.textContent = money(p) + "/oz";
    oPos.textContent = money(posVal);
    oOz.textContent = qty(goldOz) + " oz";

    // helper note
    if (req >= 1){
      const std = nearestStd(req);
      const margin = posVal / std;
      oNote.textContent = "At standard " + std + ":1, margin required = " + money(margin) +
        " (position " + money(posVal) + " ÷ " + std + ").";
    } else {
      oNote.textContent = "Your balance covers this position — no leverage needed (1:1 or less).";
    }

    empty.hidden = true;
    result.hidden = false;
  }

  [bal, lot, price, contract].forEach((el) => el.addEventListener("input", calc));
  [bal, lot, price, contract].forEach((el) => el.addEventListener("change", calc));

  calc(); // initial
})();
