odoo.define("payment_portugal.payment_form", (require) => {
    "use strict";

    const checkoutForm = require("payment.checkout_form");
    const manageForm = require("payment.manage_form");

    const paymentDemoMixin = {
        // --------------------------------------------------------------------------
        // Private
        // --------------------------------------------------------------------------

        /**
         * Simulate a feedback from a payment provider and redirect the customer to the status page.
         *
         * @override method from payment.payment_form_mixin
         * @privates
         * @param {String} code - The code of the provider
         * @param {Number} providerId - The id of the provider handling the transaction
         * @param {Object} processingValues - The processing values of the transaction
         * @returns {Promise}
         */
        _processDirectPayment: async function (code, providerId, processingValues) {
            if (!code.startsWith("mbw")) {
                return this._super(...arguments);
            }
            const phone_number = document.getElementById("phone_number").value;
            const company_id = document.getElementById("company_id").value;
            const currency = document.getElementById("currency").value;
            const route = code.endsWith("if") ? "ifthenpay" : "eupago";

            return await this._rpc({
                route: "/payment/" + route + "/mbway/feedback",
                params: {
                    reference: processingValues.reference,
                    amount: processingValues.amount,
                    currency: currency,
                    company_id: company_id,
                    phone_number: phone_number,
                },
            }).then((response) => {
                window.location = "/payment/status";
            });
        },

        /**
         * Prepare the inline form of Demo for direct payment.
         *
         * @override method from payment.payment_form_mixin
         * @private
         * @param {String} code - The code of the selected payment option's provider
         * @param {integer} paymentOptionId - The id of the selected payment option
         * @param {String} flow - The online payment flow of the selected payment option
         * @returns {Promise}
         */
        _prepareInlineForm: function (code, paymentOptionId, flow) {
            if (code.startsWith("mbw")) {
                this._setPaymentFlow("direct");
                return Promise.resolve();
            }
        },
    };
    checkoutForm.include(paymentDemoMixin);
    manageForm.include(paymentDemoMixin);
});
