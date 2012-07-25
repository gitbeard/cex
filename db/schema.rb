# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended to check this file into your version control system.

ActiveRecord::Schema.define(:version => 20120725081047) do

  create_table "companies", :force => true do |t|
    t.string   "name"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
  end

  create_table "daily_inventories", :id => false, :force => true do |t|
    t.integer  "item_number", :null => false
    t.integer  "location_id", :null => false
    t.datetime "datetime",    :null => false
    t.integer  "quantity",    :null => false
    t.integer  "file_id",     :null => false
  end

  create_table "file_infos", :force => true do |t|
    t.string   "filename",      :limit => 50, :null => false
    t.datetime "date_modified",               :null => false
    t.datetime "date_uploaded",               :null => false
  end

  add_index "file_infos", ["filename"], :name => "filename", :unique => true

  create_table "items", :primary_key => "item_number", :force => true do |t|
    t.string "alt_item_number",  :limit => 20, :null => false
    t.string "item_description", :limit => 75, :null => false
    t.string "part_number",      :limit => 20, :null => false
    t.string "part_length",      :limit => 6,  :null => false
  end

  add_index "items", ["alt_item_number"], :name => "alt_item_number", :unique => true

  create_table "parts", :force => true do |t|
    t.string   "part_number"
    t.string   "description"
    t.integer  "column"
    t.string   "column_header"
    t.string   "column_color"
    t.datetime "created_at",    :null => false
    t.datetime "updated_at",    :null => false
  end

  create_table "purchase_order_items", :force => true do |t|
    t.integer  "po_id"
    t.integer  "line_number"
    t.integer  "item_number"
    t.integer  "quantity"
    t.float    "unit_price"
    t.float    "extended_price"
    t.datetime "created_at",     :null => false
    t.datetime "updated_at",     :null => false
  end

  create_table "purchase_orders", :force => true do |t|
    t.integer  "po_number"
    t.integer  "company_id"
    t.datetime "date_placed"
    t.datetime "date_ready"
    t.datetime "date_shipped"
    t.datetime "date_received"
    t.datetime "created_at",    :null => false
    t.datetime "updated_at",    :null => false
  end

  create_table "view_distinct_part_number", :id => false, :force => true do |t|
    t.string "part_number", :limit => 20, :null => false
  end

end
