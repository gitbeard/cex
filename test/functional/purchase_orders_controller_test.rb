require 'test_helper'

class PurchaseOrdersControllerTest < ActionController::TestCase
  setup do
    @purchase_order = purchase_orders(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:purchase_orders)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create purchase_order" do
    assert_difference('PurchaseOrder.count') do
      post :create, purchase_order: { company_id: @purchase_order.company_id, date_placed: @purchase_order.date_placed, date_ready: @purchase_order.date_ready, date_received: @purchase_order.date_received, date_shipped: @purchase_order.date_shipped, po_number: @purchase_order.po_number }
    end

    assert_redirected_to purchase_order_path(assigns(:purchase_order))
  end

  test "should show purchase_order" do
    get :show, id: @purchase_order
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @purchase_order
    assert_response :success
  end

  test "should update purchase_order" do
    put :update, id: @purchase_order, purchase_order: { company_id: @purchase_order.company_id, date_placed: @purchase_order.date_placed, date_ready: @purchase_order.date_ready, date_received: @purchase_order.date_received, date_shipped: @purchase_order.date_shipped, po_number: @purchase_order.po_number }
    assert_redirected_to purchase_order_path(assigns(:purchase_order))
  end

  test "should destroy purchase_order" do
    assert_difference('PurchaseOrder.count', -1) do
      delete :destroy, id: @purchase_order
    end

    assert_redirected_to purchase_orders_path
  end
end
