class CreatePurchaseOrders < ActiveRecord::Migration
  def change
    create_table :purchase_orders do |t|
      t.integer :po_number
      t.integer :company_id
      t.datetime :date_placed
      t.datetime :date_ready
      t.datetime :date_shipped
      t.datetime :date_received

      t.timestamps
    end
  end
end
