require 'test_helper'

class PurchaseOrderItemsControllerTest < ActionController::TestCase
  setup do
    @purchase_order_item = purchase_order_items(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:purchase_order_items)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create purchase_order_item" do
    assert_difference('PurchaseOrderItem.count') do
      post :create, purchase_order_item: { extended_price: @purchase_order_item.extended_price, item_number: @purchase_order_item.item_number, line_number: @purchase_order_item.line_number, po_id: @purchase_order_item.po_id, quantity: @purchase_order_item.quantity, unit_price: @purchase_order_item.unit_price }
    end

    assert_redirected_to purchase_order_item_path(assigns(:purchase_order_item))
  end

  test "should show purchase_order_item" do
    get :show, id: @purchase_order_item
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @purchase_order_item
    assert_response :success
  end

  test "should update purchase_order_item" do
    put :update, id: @purchase_order_item, purchase_order_item: { extended_price: @purchase_order_item.extended_price, item_number: @purchase_order_item.item_number, line_number: @purchase_order_item.line_number, po_id: @purchase_order_item.po_id, quantity: @purchase_order_item.quantity, unit_price: @purchase_order_item.unit_price }
    assert_redirected_to purchase_order_item_path(assigns(:purchase_order_item))
  end

  test "should destroy purchase_order_item" do
    assert_difference('PurchaseOrderItem.count', -1) do
      delete :destroy, id: @purchase_order_item
    end

    assert_redirected_to purchase_order_items_path
  end
end
