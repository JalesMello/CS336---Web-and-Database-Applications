/**
 * Created by Jales on 5/9/2017.
 */
window.onload = function () {
    // !------------- This section of code works on the prev and next buttons within each div: ------------------------|
    // "moveSection" works by taking 2 parameters. "close" is the current div to be closed. "open" is the next/prev div to be opened
    function moveSection(close, open) {
        close.style.display = "none";
        open.style.display = "block";
    }
    // These variables get the ID's of the Next, Previous, & Submit buttons and the div's that contain them:
    var personalInfo = document.getElementById('PersonalInformation');
    var companyInfo = document.getElementById('CompanyInformation');
    var diningInfo = document.getElementById('DiningInformation');
    var workshopInfo = document.getElementById('WorkshopInformation');
    var billingInfo = document.getElementById('BillingInformation');
    var personalNextElem = document.getElementById('personalInfoNext');
    var companyPrevElem = document.getElementById('companyInfoPrev');
    var companyNextElem = document.getElementById('companyInfoNext');
    var diningPrevElem = document.getElementById('diningInfoPrev');
    var diningNextElem = document.getElementById('diningInfoNext');
    var workshopPrevElem = document.getElementById('workshopInfoPrev');
    var workshopNextElem = document.getElementById('workshopInfoNext');
    var billingPrevElem = document.getElementById('billingInfoPrev');
    // The following statements add Event Listeners to the button elements:
    personalNextElem.addEventListener('click', function(){moveSection(personalInfo, companyInfo)}, false);
    companyPrevElem.addEventListener('click', function (){moveSection(companyInfo, personalInfo)}, false);
    companyNextElem.addEventListener('click', function (){moveSection(companyInfo, diningInfo)}, false);
    diningPrevElem.addEventListener('click', function (){moveSection(diningInfo, companyInfo)}, false);
    diningNextElem.addEventListener('click', function (){moveSection(diningInfo, workshopInfo)}, false);
    workshopPrevElem.addEventListener('click', function (){moveSection(workshopInfo, diningInfo)}, false);
    workshopNextElem.addEventListener('click', function (){moveSection(workshopInfo, billingInfo)}, false);
    billingPrevElem.addEventListener('click', function (){moveSection(billingInfo, workshopInfo)}, false);

    // !------------- The below section of code deals with the radio button logic: ------------------------------------|
    function radioA (radio2Off, radio2AOn, radio2BOn, radio3On, radio3AOff, radio3BOff) {
        radio2Off.disabled = true;
        radio2AOn.checked = true;
        radio2AOn.disabled = false;
        radio2BOn.disabled = false;

        radioB(radio3On, radio3AOff, radio3BOff);
    }
    function radioB(radio3On, radio3AOff, radio3BOff) {
        radio3On.disabled = false;
        radio3On.checked = true;
        radio3AOff.disabled = true;
        radio3BOff.disabled = true;
    }
    // These variables get the ID's of the Radio buttons under the workshop section:
    var s1wsA_Elem = document.getElementById('session1wsA');
    var s1wsB_Elem = document.getElementById('session1wsB');
    var s1wsC_Elem = document.getElementById('session1wsC');
    var s2wsA_Elem = document.getElementById('session2wsA');
    var s2wsB_Elem = document.getElementById('session2wsB');
    var s2wsC_Elem = document.getElementById('session2wsC');
    var s3wsA_Elem = document.getElementById('session3wsA');
    var s3wsB_Elem = document.getElementById('session3wsB');
    var s3wsC_Elem = document.getElementById('session3wsC');
    // The following lines of code add Event Listeners to the radio button elements:
    s1wsA_Elem.addEventListener('click', function(){radioA(s2wsB_Elem, s2wsA_Elem, s2wsC_Elem, s3wsC_Elem, s3wsA_Elem, s3wsB_Elem)}, false);
    s1wsB_Elem.addEventListener('click', function(){radioA(s2wsC_Elem, s2wsA_Elem, s2wsB_Elem, s3wsC_Elem, s3wsA_Elem, s3wsB_Elem)}, false);
    s1wsC_Elem.addEventListener('click', function(){radioA(s2wsA_Elem, s2wsB_Elem, s2wsC_Elem, s3wsA_Elem, s3wsB_Elem, s3wsC_Elem)}, false);
    s2wsA_Elem.addEventListener('click', function(){radioB(s3wsC_Elem, s3wsA_Elem, s3wsB_Elem)}, false);
    s2wsB_Elem.addEventListener('click', function(){radioB(s3wsA_Elem, s3wsB_Elem, s3wsC_Elem)}, false);
    s2wsC_Elem.addEventListener('click', function(){radioB(s3wsB_Elem, s3wsA_Elem, s3wsC_Elem)}, false);
};
