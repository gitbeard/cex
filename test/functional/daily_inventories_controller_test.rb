require 'test_helper'

class DailyInventoriesControllerTest < ActionController::TestCase
  setup do
    @daily_inventory = daily_inventories(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:daily_inventories)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create daily_inventory" do
    assert_difference('DailyInventory.count') do
      post :create, daily_inventory: { datetime: @daily_inventory.datetime, file_id: @daily_inventory.file_id, item_number: @daily_inventory.item_number, location_id: @daily_inventory.location_id, quantity: @daily_inventory.quantity }
    end

    assert_redirected_to daily_inventory_path(assigns(:daily_inventory))
  end

  test "should show daily_inventory" do
    get :show, id: @daily_inventory
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @daily_inventory
    assert_response :success
  end

  test "should update daily_inventory" do
    put :update, id: @daily_inventory, daily_inventory: { datetime: @daily_inventory.datetime, file_id: @daily_inventory.file_id, item_number: @daily_inventory.item_number, location_id: @daily_inventory.location_id, quantity: @daily_inventory.quantity }
    assert_redirected_to daily_inventory_path(assigns(:daily_inventory))
  end

  test "should destroy daily_inventory" do
    assert_difference('DailyInventory.count', -1) do
      delete :destroy, id: @daily_inventory
    end

    assert_redirected_to daily_inventories_path
  end
end
