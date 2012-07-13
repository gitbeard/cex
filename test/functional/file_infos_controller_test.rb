require 'test_helper'

class FileInfosControllerTest < ActionController::TestCase
  setup do
    @file_info = file_infos(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:file_infos)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create file_info" do
    assert_difference('FileInfo.count') do
      post :create, file_info: { date_modified: @file_info.date_modified, date_uploaded: @file_info.date_uploaded, filename: @file_info.filename }
    end

    assert_redirected_to file_info_path(assigns(:file_info))
  end

  test "should show file_info" do
    get :show, id: @file_info
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @file_info
    assert_response :success
  end

  test "should update file_info" do
    put :update, id: @file_info, file_info: { date_modified: @file_info.date_modified, date_uploaded: @file_info.date_uploaded, filename: @file_info.filename }
    assert_redirected_to file_info_path(assigns(:file_info))
  end

  test "should destroy file_info" do
    assert_difference('FileInfo.count', -1) do
      delete :destroy, id: @file_info
    end

    assert_redirected_to file_infos_path
  end
end
