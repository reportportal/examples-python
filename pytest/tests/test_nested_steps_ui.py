#  Copyright (c) 2022 https://reportportal.io .
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License
"""A test which shows how UI test with nested steps might look like."""
import logging

from reportportal_client import step

from tests.ui.web import OrderingSimulator

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

order_simulator = OrderingSimulator()


@step
def navigate_to_main_page():
    logger.info('Main page displayed')


@step
def login():
    order_simulator.log_in()
    logger.info('User logged in')


@step
def navigate_to_products_page():
    products = order_simulator.get_products()
    logger.info('Products page opened')
    return products


@step
def click_on_product():
    product = order_simulator.choose_product()
    logger.info("Product click event")
    return product


@step
def select_products_count(count):
    logger.info(str(count) + " products selected")


@step
def click_cart_button(product, count):
    order_simulator.add_product(product, count)
    logger.info(str(count) + " products added to the cart")
    assert 5 == count


@step
def add_product_to_cart(product_count):
    product = click_on_product()
    select_products_count(product_count)
    click_cart_button(product, product_count)


@step
def pay(total_price):
    order_simulator.do_payment(total_price)
    logger.info("Successful payment")


@step
def logout():
    order_simulator.log_out()
    logger.info("User logged out")


def test_order_products():
    product_count = 5
    price = 3.0
    total_price = price * product_count

    navigate_to_main_page()
    login()
    navigate_to_products_page()
    add_product_to_cart(product_count)
    pay(total_price)
    logout()
