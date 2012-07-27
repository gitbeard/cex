class AddPartNumberToPurchaseOrderItems < ActiveRecord::Migration
  def change
    add_column :purchase_order_items, :part_number, :string, :after => :item_number
    add_column :purchase_order_items, :part_description, :string, :after => :part_number
    add_column :purchase_order_items, :status, :integer, :after => :extended_price
  end
end
