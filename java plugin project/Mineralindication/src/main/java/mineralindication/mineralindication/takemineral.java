package mineralindication.mineralindication;

import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.Sound;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.inventory.ItemStack;

import java.sql.*;
import java.util.UUID;

public class takemineral implements CommandExecutor{

    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        final Player p = (Player) sender;
        UUID id = p.getUniqueId();
        String ID = String.valueOf(p);
        String q1 = "CraftPlayer{name=";
        String q2 = "}";
        String q3 = ID.replace(q1, "").replace(q2, "");
        String ip = Mineralindication.getMain().getConfig().getString("SQL.ip");
        String table = Mineralindication.getMain().getConfig().getString("SQL.table");
        String user = Mineralindication.getMain().getConfig().getString("SQL.user");
        String password = Mineralindication.getMain().getConfig().getString("SQL.password");
        String DB_DRIVER = "com.mysql.jdbc.Driver";
        String DB_URL = "jdbc:mysql://" + ip + "/" + table;
        String DB_USERNAME = user;
        String DB_PASSWORD = password;
        try(Connection conn1 = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            Statement stmt1 = conn1.createStatement();
            Statement stmt2 = conn1.createStatement();
            ResultSet rs = stmt2.executeQuery("SELECT * FROM takemineral where token = ('"+args[0]+"')");
        ) {
            rs.next();
            int iron = rs.getInt("iron");
            int coal = rs.getInt("emerald");
            int diamond = rs.getInt("diamond");
            int copper = rs.getInt("copper");
            int redstone = rs.getInt("redstone");
            int gold = rs.getInt("gold");
            int emerald = rs.getInt("emerald");
            ItemStack Itemiron = new ItemStack(Material.RAW_IRON,iron);
            ItemStack Itemcoal = new ItemStack(Material.COAL,coal);
            ItemStack Itemdiamond = new ItemStack(Material.DIAMOND,diamond);
            ItemStack Itemcopper = new ItemStack(Material.RAW_COPPER,copper);
            ItemStack Itemredstone = new ItemStack(Material.REDSTONE,redstone);
            ItemStack Itemgold = new ItemStack(Material.RAW_GOLD,gold);
            ItemStack Itememerald = new ItemStack(Material.EMERALD,emerald);
            p.getInventory().addItem(new ItemStack(Itemiron));
            p.getInventory().addItem(new ItemStack(Itemcoal));
            p.getInventory().addItem(new ItemStack(Itemdiamond));
            p.getInventory().addItem(new ItemStack(Itemcopper));
            p.getInventory().addItem(new ItemStack(Itemredstone));
            p.getInventory().addItem(new ItemStack(Itemgold));
            p.getInventory().addItem(new ItemStack(Itememerald));
            String sql = "DELETE FROM takemineral WHERE token = ('"+args[0]+"')";
            stmt1.executeUpdate(sql);
            p.sendMessage(ChatColor.GREEN + "SUCESSFUL TAKEN THE MINERAL FROM YOUR BANK ACCOUNT");
            p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
        }
        catch (SQLException ed) {
            ed.printStackTrace();
            p.sendMessage(ChatColor.RED + "THE TOKEN MAY NOT EXIST");
        }

        return false;}
}
