class AddLineItemsToPurchaseOrders < ActiveRecord::Migration
  def change
    add_column :purchase_orders, :line_items, :integer, :after => :company_id
    add_column :purchase_orders, :total_items, :integer, :after => :line_items
    add_column :purchase_orders, :total_price, :float, :after => :total_items
    add_column :purchase_orders, :status, :integer, :after => :total_price
  end
end
